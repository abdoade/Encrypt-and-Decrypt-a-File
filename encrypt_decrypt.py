from cryptography.fernet import Fernet
#keyاول حاجة لازم نولد  
# symmetricعلشان هنشفر بيه وهنفك بنفس التشفير دي طريقة
def generate_key():
    key = Fernet.generate_key()     #fernet جزء من مكتبة cryptography هنستخدمها في التشفير وفك التشفير بنفس المفتاح
    with open("secret.key", "wb") as key_file: #هنفتح ملف باسم secret.key في وضع الكتابة الثانية ("wb") ليه wb علشان هيتخزن كبيانات ثنائية مش ملف txt
        key_file.write(key)

# هنا هنقراء المفتاح اللي تم حفظه 
def load_key():
    return open("secret.key", "rb").read() #("rb") وضع القراء الثنائية 

# تشفير البيانات
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key) #هتاخد object من class Fernet وهيحتوي المفتاح اللي تم انشائه
    with open(filename, "rb") as file:
        file_data = file.read() #هنبدا نخزن الداتا المراد تشفيرها
    encrypted_data = fernet.encrypt(file_data) #هنا تم تشفير الداتا وتخيزنها 
    with open(filename, "wb") as file:# هنبدا نبدل الداتا الموجده بالمشفرة
        file.write(encrypted_data) 
    print("File encrypted successfully!") 


def decrypt_file(filename):
    key = load_key()        
    fernet = Fernet(key)
    with open(filename, "rb") as file: 
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data) #هنا زي الدالة التشفير لكن الاختلاف فقد في فك التشفير )(fernet.decrypt)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully!")

# الاستخدام
#generate_key()  # يتم تنفيذ هذه الخطوة مرة واحدة فقط لإنشاء مفتاح التشفير

filename = "data_file.txt"  # اسم الملف المراد تشفيره
#encrypt_file(filename)  # تشفير الملف
decrypt_file(filename)  # فك تشفير الملف
