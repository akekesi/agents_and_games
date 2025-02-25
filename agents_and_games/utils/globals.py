import os


suffix  ="test"
game_name = "TicTacToe"
agent_name = "AgentMinimax"
name_subdir = f"{game_name}_{agent_name}_{suffix}"

PATH_DATA_DIR = os.path.join(os.path.dirname(__file__),"..", "data", name_subdir)
PATH_DATA_CSV = os.path.join(PATH_DATA_DIR, "game_data.csv")
PATH_MODEL_PTH = os.path.join(PATH_DATA_DIR, "model.pth")
PATH_MODEL_LOSSES_CSV = os.path.join(PATH_DATA_DIR, "model_losses.csv")
PATH_MODEL_ACCURACY_CSV = os.path.join(PATH_DATA_DIR, "model_accuracy.csv")
PATH_DATA_CSV_TRAIN = PATH_DATA_CSV.replace(".csv", "_train.csv")
PATH_DATA_CSV_TEST = PATH_DATA_CSV.replace(".csv", "_test.csv")
