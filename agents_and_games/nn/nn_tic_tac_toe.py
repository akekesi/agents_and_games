import torch
import pandas as pd


class TicTacToeNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(9, 128)  # First hidden layer
        self.fc2 = torch.nn.Linear(128, 64) # Second hidden layer
        self.fc3 = torch.nn.Linear(64, 9)   # Output layer (one for each position)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)  # No softmax here, since CrossEntropyLoss will handle it
        return x


def train(model, train_loader, test_loader, path_model_pth, epochs=10):
    best_val_loss = float('inf')
    avg_train_losses = []
    avg_val_losses = []

    loss_fn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(epochs):
        # Training Phase
        model.train()
        total_train_loss = 0
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = loss_fn(outputs, y_batch)
            loss.backward()
            optimizer.step()
            total_train_loss += loss.item()

        avg_train_loss = total_train_loss / len(train_loader)

        # Validation Phase
        model.eval()
        total_val_loss = 0
        with torch.no_grad():
            for X_val, y_val in test_loader:
                val_outputs = model(X_val)
                val_loss = loss_fn(val_outputs, y_val)
                total_val_loss += val_loss.item()

        avg_val_loss = total_val_loss / len(test_loader)

        avg_train_losses.append(avg_train_loss)
        avg_val_losses.append(avg_val_loss)

        # Print losses
        print(f"Epoch {epoch+1}/{epochs}, Train Loss: {avg_train_loss:.4f}, Validation Loss: {avg_val_loss:.4f}")

        # Save only the best model
        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            torch.save(model.state_dict(), path_model_pth)
            print(f"New best model saved (Validation Loss: {avg_val_loss:.4f})")

    # Create a DataFrame
    df = pd.DataFrame({
        "epoch": list(range(epochs)),
        "avg_train_loss": avg_train_losses,
        "avg_val_loss": avg_val_losses,
    })

    # Save as CSV
    path_losses_csv = path_model_pth.replace(".pth", "_losses.csv")
    df.to_csv(path_losses_csv, index=False)


def load_trained_model(model, path_model_trained):
    model.load_state_dict(torch.load(path_model_trained))
    model.eval()
    return model


def evaluate(model, test_loader, path_accuracy_csv):
    model.eval()  # TODO: Check if this is necessary
    moves_correct = 0
    moves_total = 0

    with torch.no_grad():
        for X_batch, y_batch in test_loader:
            outputs = model(X_batch)
            predictions = torch.argmax(outputs, dim=1)
            moves_correct += (predictions == y_batch).sum().item()
            moves_total += y_batch.size(0)

    accuracy = moves_correct / moves_total
    print(f"Test Accuracy: {accuracy * 100:.2f}%")
    df = pd.DataFrame({
        "moves_correct": [moves_correct],
        "moves_total": [moves_total],
        "accuracy": [accuracy],
    })

    # Save as CSV
    df.to_csv(path_accuracy_csv, index=False)


def get_move(model, board):
    model.eval()  # TODO: Check if this is necessary
    board_tensor = torch.tensor(board.flatten(), dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        output = model(board_tensor)
        move_idx = torch.argmax(output).item()

    return divmod(move_idx, 3)  # Convert back to (row, col)
