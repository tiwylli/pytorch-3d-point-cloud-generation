import csv
import matplotlib.pyplot as plt
import numpy as np

# Chemin vers le fichier CSV
fichier_csv = './logs/ORIG_STG1_lc_thingi10k.csv'
epochs = []
train_losses = []
val_losses = []
def plot_loss_from_epoch(csv_file, start_epoch=0):
    # Listes pour stocker les données
    epochs = []
    train_losses = []
    val_losses = []

    # Lecture des données depuis le fichier CSV
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            epoch = int(row['epoch'])
            if epoch >= start_epoch:
                epochs.append(epoch)
                train_losses.append(float(row['train_loss']))
                val_losses.append(float(row['val_loss']))
    return epochs, train_losses, val_losses

epochs, train_losses, val_losses = plot_loss_from_epoch(fichier_csv, 0)

# Tracer le graphique
plt.plot(epochs, train_losses, label='Train Loss')
#plt.plot(epochs, val_losses, label='Validation Loss')
#plt.plot(epochs, np.log(val_losses), label='Log Validation Loss')

# Ajouter des titres et légendes
plt.title('Évolution des pertes entrainement')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Afficher le graphique
plt.savefig('thingi_s1_train.png')
