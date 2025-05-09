# 🧠 Python Virtual Environment Setup Guide (Windows, Linux & macOS)

Set up and manage your machine learning project in a clean Python environment using the steps below.

---

## 🛠️ Step 1: Create Virtual Environment

```bash
python -m venv my_ml_env
```

---

## 📁 Step 2: Navigate to Your Project Folder

```bash
cd path/to/your_project_folder
# Example for Windows:
# cd C:\ML_Projects\your_project_folder
```

---

## ▶️ Step 3: Activate the Virtual Environment

**Windows:**

```bash
my_ml_env\Scripts\activate
```

**macOS/Linux:**

```bash
source my_ml_env/bin/activate
```

After activation, your terminal prompt will look like this:

```bash
(my_ml_env) your_project_folder>
```

---

## 📦 Step 4: Check Installed Packages (Optional)

```bash
pip list
```

---

## ❌ Step 5: Deactivate the Virtual Environment

```bash
deactivate
```

---

## 📄 Step 6: Generate `requirements.txt`

```bash
pip freeze > requirements.txt
```

---

## 📥 Step 7: Install Packages from `requirements.txt`

```bash
pip install -r requirements.txt
```

---

✅ You're now ready to work in a clean and portable Python environment for your machine learning project!

