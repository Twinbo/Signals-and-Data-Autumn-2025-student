import os

import numpy as np
import torch
from sklearn.metrics import confusion_matrix, recall_score
from tqdm.notebook import tqdm
from plotting_function import plot_metrics


def train(model, train_dataloader, epochs=1, overwrite=False, val_dataloader=None, run_filepath="", plot=False):
    # To hold accuracy and confusion matrices during training and testing
    train_accs = []
    test_accs = []
    confusion_matrices = []
    val_sensitivities = []
    val_specificities = []

    for epoch in tqdm(range(epochs), desc='Training'):

        path_epoch = os.path.join(run_filepath, f"{epoch}.pth")
        os.makedirs(os.path.dirname(path_epoch), exist_ok=True)
        if overwrite or not os.path.exists(path_epoch):

            epoch_acc = 0
            all_targets = []
            all_preds = []

            for inputs, targets in tqdm(train_dataloader):
                logits = model(inputs)
                loss = model.criterion(logits, targets.flatten())
                loss.backward()

                model.optim.step()
                model.optim.zero_grad()

                # Not actually used for training, just for keeping track of accuracy
                epoch_acc += (torch.argmax(logits, dim=1) == targets).sum().item()

                # Store targets and predictions for confusion matrix
                all_targets.extend(targets.numpy())
                all_preds.extend(torch.argmax(logits, dim=1).numpy())

            model.save_model(path_epoch)
            train_accs.append(epoch_acc / len(all_targets))
            print(f"Epoch {epoch} training accuracy: {epoch_acc / len(all_targets)}")

        else:
            train_accs.append(np.nan)
            model.load_model(path_epoch)
            print(f"Loaded model from {path_epoch}. Skipping epoch.")

        # If we have val dataloader, we can evaluate after each epoch
        if val_dataloader is not None:
            val_targets, val_preds = [], []
            model.eval()  # Ensure the model is in evaluation mode
            with torch.no_grad():
                for val_inputs, val_targets_batch in val_dataloader:
                    val_logits = model(val_inputs)
                    val_preds_batch = torch.argmax(val_logits, dim=1)
                    val_targets.extend(val_targets_batch.numpy())
                    val_preds.extend(val_preds_batch.numpy())

            # Calculate validation accuracy
            val_acc = (np.array(val_preds) == np.array(val_targets)).mean()
            test_accs.append(val_acc)
            print(f"Epoch {epoch} validation accuracy: {val_acc}")

            # Compute validation confusion matrix, sensitivity, and specificity
            cm_val = confusion_matrix(val_targets, val_preds)
            sensitivity_val = recall_score(val_targets, val_preds, average=None)

            # Calculate specificity for each class
            tn_val = cm_val.sum(axis=1) - cm_val.diagonal()
            specificity_val = tn_val / (tn_val + cm_val.sum(axis=0) - cm_val.diagonal())

            # Append to lists
            confusion_matrices.append(cm_val)
            val_sensitivities.append(sensitivity_val)
            val_specificities.append(specificity_val)

            print(f"Validation Sensitivity for epoch {epoch}: {sensitivity_val}")
            print(f"Validation Specificity for epoch {epoch}: {specificity_val}")

        if plot:
            plot_metrics(train_accs, test_accs, val_sensitivities, val_specificities, confusion_matrices)

    return train_accs, test_accs, confusion_matrices, val_sensitivities, val_specificities