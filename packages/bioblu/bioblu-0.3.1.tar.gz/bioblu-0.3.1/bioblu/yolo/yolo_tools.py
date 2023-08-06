#!/usr/bin/env python3
import contextlib
import os
import platform
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import sys
import datetime
from typing import List, Union
import warnings

import tensorflow as tf

from bioblu.ds_manage import ds_convert
from bioblu.ds_manage import ds_annotations


def save_confmat(array: np.ndarray, names: List[str], fdir_dst: str = "/home/findux/Desktop/"):
    """To be used inside the Confusion Matrix class that comes with yolov5"""
    tstamp = str(format(datetime.datetime.now(), "%Y%m%d_%H%M"))
    savename = f"{fdir_dst}confusion_matrix_{tstamp}.csv"
    print(tstamp)
    cmlabs = names + ["background"]
    cm_df = pd.DataFrame(array, columns=cmlabs)
    cm_df["Predicted"] = cmlabs
    cm_df.set_index("Predicted", inplace=True)
    cm_df.to_csv(savename)

def get_class_names_from_weights_file(fpath_yolo_model_weights: str, yolo_dir: str) -> list:
    sys.path.insert(0, yolo_dir)
    map_location = torch.device('cpu')
    weights = torch.load(fpath_yolo_model_weights, map_location=map_location)
    names: list = weights["model"].names
    return names


def overwrite_class_names_in_yolo_weights_file(fpath_yolo_weights_file, rename_dict: dict, yolo_dir, fpath_dst=None,
                                               duplicate_names_ok=False, overwrite_ok=False):
    """UNTESTED"""
    sys.path.insert(0, yolo_dir)

    # Make lowercase
    rename_dict = {k.lower(): v.lower() for k, v in rename_dict.items()}

    weights = torch.load(fpath_yolo_weights_file)
    old_names = [n.lower() for n in weights["model"].names]

    if not duplicate_names_ok:
        assert len(rename_dict) == len(set(list(rename_dict.values())))

    new_names = []
    for old in old_names:
        if old in rename_dict.keys():
            print(f"Overwriting <{old}> with <{rename_dict[old]}>")
            new_names.append(rename_dict[old])
        else:
            new_names.append(old)

    if not duplicate_names_ok:
        assert len(new_names) == len(set(new_names))

    weights["model"].names = new_names

    if fpath_dst is None and overwrite_ok:
        fpath_dst = fpath_yolo_weights_file
    elif fpath_dst is None and not overwrite_ok:
        base, ext = os.path.splitext(fpath_yolo_weights_file)
        fpath_dst = f"{base}_renamed{ext}"
    elif fpath_dst is not None:
        if not overwrite_ok:
            if os.path.exists(fpath_dst):
                raise FileExistsError("Pass overwrite_ok=True to overwrite existing files.")
    torch.save(weights, fpath_dst)


# def get_yolo_iou(yolo_bbox_1: List[float], yolo_bbox_2: List[float]) -> float:
#     """
#     Gets the iou value of yolo bboxes.
#     :param yolo_bbox_1: [cx, cy, w, h] (relative)
#     :param yolo_bbox_2: [cx, cy, w, h] (relative)
#     :return:
#     """
#     ds_convert.cvt_coco_box_to_voc_dict()


def get_TP_FP_FN_GT_NAMES(fdir_annotations_set, fdir_predictions, iou_thresh: float = 0.25, pred_conf_thresh=None,
                      plot=False):
    """Returns five lists: TP per img, FN per img, FP per img, GT per img, names ."""
    all_ground_truths = ds_annotations.get_all_fpaths_by_extension(fdir_annotations_set, (".txt",))

    img_names = []
    TP_per_img = []
    FN_per_img = []
    GT_per_img = []
    FP_per_img = []

    for fpath_gt in all_ground_truths:
        img_names.append(ds_annotations.get_basename_only(fpath_gt))
        ground_truths = ds_annotations.load_yolo_annotation_only(fpath_gt)

        TP = 0
        FP = 0  # FN and GT are calculated when appended at the end of the loop

        # Go over the predictions
        preds_fpath = ds_annotations.get_corresponding_file(fpath_gt, fdir_predictions)
        if preds_fpath is not None:  # If nothing was detected, there is no predictions file
            preds = ds_annotations.load_yolo_annotation_only(preds_fpath)

            if pred_conf_thresh is not None:
                preds = [p for p in preds if p["confidence"] >= pred_conf_thresh]

            # Get TP count
            for GT in ground_truths:
                gt_bbox: dict = ds_convert.cvt_yolo_box_to_relative_voc_dict(GT["bbox"])
                for pred in preds:
                    pred_bbox: dict = ds_convert.cvt_yolo_box_to_relative_voc_dict(pred["bbox"])
                    iou = ds_annotations.get_iou(gt_bbox, pred_bbox)
                    if iou >= iou_thresh:
                        TP += 1
                        break  # One TP is enough per GT
            # Get FP count
            for pred in preds:
                pred_bbox: dict = ds_convert.cvt_yolo_box_to_relative_voc_dict(pred["bbox"])
                has_no_GT = True
                for GT in ground_truths:
                    gt_bbox: dict = ds_convert.cvt_yolo_box_to_relative_voc_dict(GT["bbox"])
                    iou = ds_annotations.get_iou(pred_bbox, gt_bbox)
                    if iou > iou_thresh:
                        has_no_GT = False  # bbox HAS a ground truth
                if has_no_GT:  # If no GT was found to overlap with this prediction:
                    FP += 1


        TP_per_img.append(TP)
        FP_per_img.append(FP)
        GT_per_img.append(len(ground_truths))
        FN_per_img.append(len(ground_truths) - TP)

    assert (sum(TP_per_img) + sum(FN_per_img)) == sum(GT_per_img)

    return TP_per_img, FP_per_img, FN_per_img, GT_per_img, img_names


def create_yolo_ds_yaml(fpath_target_dir: str, materials_dict: dict, include_test_set=True) -> str:
    """Creates a yolo dataset yaml file in the directory and returns the path to it"""

    fpath_dst = os.path.join(fpath_target_dir, "dataset.yaml")

    lines = ["# Dataset paths"]
    lines.append(f"path: {fpath_target_dir} # DS oot dir")
    lines.append(f"train: {os.path.join(fpath_target_dir, 'images', 'train')}")
    lines.append(f"val: {os.path.join(fpath_target_dir, 'images', 'valid')}")
    if include_test_set:
        lines.append(f"test: {os.path.join(fpath_target_dir, 'images', 'test')}")

    lines.append("# Classes")
    lines.append(f"nc: {len(materials_dict)}")
    lines.append(f"names: {list(materials_dict.values())}")

    lines = [l + "\n" for l in lines if not l.endswith("\n")]

    with open(os.path.join(fpath_dst), "w") as f:
        f.writelines(lines)


def get_metrics_df(fdir_annotations, fdir_predictions, iou_thresh=0.5, pred_conf_thresh=None):
    """Returns precision and recall"""
    TP, FP, FN, GT, fnames = get_TP_FP_FN_GT_NAMES(fdir_annotations, fdir_predictions, iou_thresh, pred_conf_thresh)
    metrics_df = pd.DataFrame({"image_name": fnames, "TP": TP, "FP": FP, "FN": FN, "GT": GT})
    return metrics_df


def get_precision_recall(fdir_annotations, fdir_predictions, iou_thresh=0.5, pred_conf_thresh=None):
    metrics_df = get_metrics_df(fdir_annotations, fdir_predictions, iou_thresh, pred_conf_thresh)
    metrics_df["recall"] = metrics_df["TP"] / (metrics_df["GT"])
    recall = metrics_df["TP"].sum() / metrics_df["GT"].sum()
    precision = metrics_df["TP"].sum() / (metrics_df["TP"].sum() + metrics_df["FP"].sum())
    return precision, recall


def get_predictions_per_gt(fdir_gt_labels, fdir_gt_imgs, fdir_pred_labels, fdir_pred_imgs, materials_dict,
                           iou_threshold=0.5, conf_threshold=None, plot_hist=False):
    #  ToDo: Instead of all this, write a yolo-predictions-to-coco parser.
    ground_truths: List[List[dict]] = [ds_annotations.load_yolo_annotation_only(fpath) for fpath
                                       in sorted(os.listdir(fdir_gt_labels))
                                       if fpath.endswith(".txt")]
    predictions: List[List[dict]] = [ds_annotations.load_yolo_annotation_only(fpath) for fpath
                                     in sorted(os.listdir(fdir_pred_labels))
                                     if fpath.endswith(".txt")]
    # Filter out those below conf_threshold:
    # if conf_threshold is not None:
    #     ground_truths = "FUCK"
    #
    # predictions_per_gt = []
    # avg_ppgt_per_img = []
    # img_names = []
    # for img in ground_truths["images"]:
    #     img_names.append(os.path.split(img["file_name"])[-1])
    #     img_ppgts = []
    #     img_GTs = [gt for gt in ground_truths["annotations"] if gt["image_id"] == img["id"]]
    #     img_preds = [p for p in predictions if p["image_id"] == img["id"]]
    #     for GT in img_GTs:
    #         pred_count = 0
    #         GT_bbox: dict = ds_convert.cvt_coco_box_to_voc_dict(GT["bbox"])
    #         for P in img_preds:
    #             P_bbox: dict = ds_convert.cvt_coco_box_to_voc_dict(P["bbox"])
    #             if ds_annotations.get_iou(GT_bbox, P_bbox) >= iou_threshold:
    #                 pred_count += 1
    #         predictions_per_gt.append(pred_count)
    #         img_ppgts.append(pred_count)
    #     avg_ppgt_per_img.append(np.mean(np.array(img_ppgts)))
    #
    # if plot_hist:
    #     counts = pd.DataFrame({"Preds_per_GT": predictions_per_gt})
    #     fig, ax = plt.subplots()
    #     ax.hist(counts,)
    #     ax.set_title(f"Frequency of predictions per groundtruth\n"
    #                  f"Thresholds: IoU: {iou_threshold}, conf.: {conf_threshold}\n"
    #                  f"Dataset: {gt_json}")
    #     plt.show()
    #
    # ppgt_per_img = pd.DataFrame({"Image_name": img_names, "Avg_pred_per_GT": avg_ppgt_per_img})
    #
    # return predictions_per_gt, ppgt_per_img


def get_box_size_density_dist():
    """Maybe use px area?"""
    pass


def detect(fpath_weights, fpath_yolo_repo, fpath_imgs, iou_threshold, conf_threshold):
    pass  # ToDo


def get_conf_matrix_subset():
    pass # ToDo


def get_wh_ratio(yolo_bbox: Union[List[float], np.array, tf.Tensor]):
    """expects yolo bbox format: [class, x_center, y_center, width, height, (conf optional)]"""
    yolo_bbox = np.array(yolo_bbox).astype("float32")  # Align possible different input dtypes
    print(yolo_bbox)
    assert 5 <= len(yolo_bbox) <= 6
    width = yolo_bbox[3]
    height = yolo_bbox[4]
    return width / height


if __name__ == "__main__":
    # model = "/media/findux/DATA/Documents/Malta_II/results/7050_2022-07-22_175457/train/exp/weights/7050_best.pt"
    # model = "/media/findux/DATA/Documents/Malta_II/results/Catania/best_multi.pt"
    # yolov5 = "/media/findux/DATA/Documents/Malta_II/yolov5/"
    # print(get_class_names_from_weights_file(model, yolov5))

    # t1 = tf.constant([0, 0.76, 0.8, 0.12, 0.2])
    # print(get_wh_ratio(t1))
    #
    # t1 = [0, 0.76, 0.8, 0.12, 0.2]
    # print(get_wh_ratio(t1))

    matrix = np.array([[2, 1, 2],
                       [4, 3, 2],
                       [5, 3, 8]])
    names = ["Foo", "bar"]
    save_confmat(matrix, names)