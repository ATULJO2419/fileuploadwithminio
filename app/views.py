from django.shortcuts import render, get_object_or_404

from .models import Document
from django.contrib import messages

# for encryption 
from django.contrib.auth.decorators import user_passes_test
from cryptography.fernet import Fernet


def encrypt_content(content):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_content = cipher_suite.encrypt(content)
    return key,encrypted_content


def decrypt_content(key,encrypted_content):
    cipher_suite = Fernet(key)
    decrypted_content=cipher_suite.decrypt(encrypted_content)  
    return decrypted_content


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        documents = request.FILES.getlist("documents")
        documents_list = []

        for document in documents:
            try:
                with document.open('rb') as file:
                    content = file.read()
                    key, encrypted_content = encrypt_content(content)

                doc = Document(name=name, document=document)
                doc.key = key
                doc.encrypted_content = encrypted_content
                doc.save()
                documents_list.append(doc)

            except Exception as e:
                # Handle any exceptions, log, or display an error message
                print(f"Error processing file: {e}")

        messages.success(request, "Documents Uploaded")

    return render(request, "index.html")

@user_passes_test(lambda u : u.is_staff )
def admin_view(request, document_id):
    document = get_object_or_404(Document,pk =document_id)

    decrypted_content= decrypt_content(document.key, document.encrypted_content)

    # pass the decrypted content to the template of admin_view

    return render(request, "admin_view.html", {"decrypted_content": decrypted_content})
