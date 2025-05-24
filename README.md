# 🔒 File Encryption and Decryption using Python and `cryptography`

## السلام عليكم النهارده هنتكلم عن ازاي تشفر بياناتك و تفكها باستخدام لغة البرمجة `python` واتمني ان يعجبكم شرحي :)


---

## 💡 Prerequisites

#### اولا لازم نعمل تثبيت لمكتبة `cryptography` 

```bash
pip install cryptography
```

## 📝 Code Explanation

### 1️⃣ Step 1: Generate a Symmetric Key

```python
from cryptography.fernet import Fernet
#keyاول حاجة لازم نولد  
# symmetricعلشان هنشفر بيه وهنفك بنفس التشفير دي طريقة
def generate_key():
    key = Fernet.generate_key()     #fernet جزء من مكتبة cryptography هنستخدمها في التشفير وفك التشفير بنفس المفتاح
    with open("secret.key", "wb") as key_file: #هنفتح ملف باسم secret.key في وضع الكتابة الثانية ("wb") ليه wb علشان هيتخزن كبيانات ثنائية مش ملف txt
        key_file.write(key)
```

### 2️⃣ Step 2: Load the Key

```python
def load_key(): #هنقراء المفتاح اللي اتولد
    return open("secret.key", "rb").read() #("rb") وضع القراء الثنائية 

```

### 3️⃣ Step 3: Encrypt a File

```python
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key) #هتاخد object من class Fernet وهيحتوي المفتاح اللي تم انشائه
    with open(filename, "rb") as file:
        file_data = file.read() #هنبدا نخزن الداتا المراد تشفيرها
    encrypted_data = fernet.encrypt(file_data) #هنا تم تشفير الداتا وتخيزنها 
    with open(filename, "wb") as file:# هنبدا نبدل الداتا الموجده بالمشفرة
        file.write(encrypted_data) 
    print("File encrypted successfully!") 
```


### 4️⃣ Step 4: Decrypt a File

```python
def decrypt_file(filename):
    key = load_key()        
    fernet = Fernet(key)
    with open(filename, "rb") as file: 
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data) #هنا زي الدالة التشفير لكن الاختلاف فقد في فك التشفير )(fernet.decrypt)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully!")
```

- **لاحظو ان احنا استخدمنا وضع الكتابة الثنائية و وضع القراءة الثنائية علشان نخزن المفتاح كبيانات ثنائية (wb) (rb)**

---

## 🚀 Usage

1. **Generate the key** هنا هنستخدمه مرة واحدة فقط ولازم يكون في مكان secure):

    ```python
    generate_key()
    ```

2. **Encrypt a file** هنعمل passing لاسم الملف المراد تشفيره `encrypt_file` function:

    ```python
    filename = "file_data.txt"  # Example filename
    encrypt_file(filename)  # Encrypt the file
    ```

3. **Decrypt a file** هنعمل passing لاسم الملف المراد تشفيره `decrypt_file` function:

    ```python
    decrypt_file(filename)  # Decrypt the file
    ```

---

## ⚠️ Important Security Notes

- **حافظ على أمان ملف `secret.key`**: هذا الملف أساسي لفك تشفير الملفات. إذا فقدته، لن تتمكن من فك تشفير الملفات المشفرة.
  
- **احفظ نسخة احتياطية من الملفات الأصلية**: لأن هذا الكود يستبدل محتوى الملف الأصلي بالبيانات المشفرة، يُفضل الاحتفاظ بنسخة غير مشفرة كنسخة احتياطية.

- **لا تشارك المفتاح**: مشاركة المفتاح تعرض الأمان للخطر، حيث سيتمكن أي شخص يمتلك المفتاح من فك تشفير ملفاتك.

---

## 🎉 Congratulations!
### اتمني لو في اي نصيحه ممكن متتاخرش كلنا بتعلم من بعض ;)
