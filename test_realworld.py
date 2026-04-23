import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# =========================
# LOAD MODELS
# =========================
basic_model     = load_model("notebooks/models/basic_cnn_model.keras")
mobilenet_model = load_model("notebooks/models/mobilenetv2_finetuned.keras")

# =========================
# LOAD CLASS NAMES
# =========================
with open("notebooks/models/class_names.json", "r") as f:
    class_names = json.load(f)

# =========================
# DATASET PATH (TRAIN DATA)
# =========================
DATASET_PATH = r"E:\Files\Downloads\PlantDiseaseProject\dataset\Plant_leave_diseases_dataset_with_augmentation"

# =========================
# TEST LOOP
# =========================
basic_correct     = 0
mobilenet_correct = 0
total             = 0

per_class_results = []

print("\n📊 Testing on TRAINED DATASET...\n")

for class_name in class_names:
    folder = os.path.join(DATASET_PATH, class_name)

    if not os.path.exists(folder):
        print(f"[SKIP] {class_name}")
        continue

    images = [f for f in os.listdir(folder)
              if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    cls_basic = 0
    cls_mob   = 0
    cls_total = 0

    # 🔥 LIMIT images (IMPORTANT to avoid long runtime)
    images = images[:100]   # test only 100 per class

    for img_file in images:
        try:
            img = Image.open(os.path.join(folder, img_file)).convert("RGB").resize((160, 160))
            arr = np.expand_dims(image.img_to_array(img), axis=0) / 255.0

            pred_basic = class_names[np.argmax(basic_model.predict(arr, verbose=0))]
            pred_mob   = class_names[np.argmax(mobilenet_model.predict(arr, verbose=0))]

            if pred_basic == class_name:
                cls_basic += 1
            if pred_mob == class_name:
                cls_mob += 1

            cls_total += 1

        except Exception as e:
            print(f"[ERROR] {img_file}: {e}")

    basic_correct     += cls_basic
    mobilenet_correct += cls_mob
    total             += cls_total

    b_acc = (cls_basic / cls_total * 100) if cls_total > 0 else 0
    m_acc = (cls_mob   / cls_total * 100) if cls_total > 0 else 0

    per_class_results.append((class_name, cls_total, b_acc, m_acc))

    print(f"✅ {class_name:<40} | imgs: {cls_total:>3} | BasicCNN: {b_acc:>6.1f}% | MobileNetV2: {m_acc:>6.1f}%")

# =========================
# FINAL RESULTS
# =========================
print("\n" + "=" * 80)
print(f"{'Class':<40} | {'Images':>6} | {'BasicCNN':>10} | {'MobileNetV2':>12}")
print("=" * 80)

for cls, n, b, m in per_class_results:
    print(f"{cls:<40} | {n:>6} | {b:>9.1f}% | {m:>11.1f}%")

print("=" * 80)

print(f"\n📊 TOTAL IMAGES TESTED: {total}")
print(f"Basic CNN Accuracy   : {(basic_correct/total)*100:.2f}%")
print(f"MobileNetV2 Accuracy : {(mobilenet_correct/total)*100:.2f}%")
print("=" * 80)