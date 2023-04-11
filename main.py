import base64

import requests
import streamlit as st

from scheme import PersonInfo

SERVICE_ADDRESS_HOST = "5.23.52.136"
SERVICE_ADDRESS_PORT = "8001"
SERVICE_ADDRESS = f"http://{SERVICE_ADDRESS_HOST}:{SERVICE_ADDRESS_PORT}"


def signup():
    st.subheader("Sign Up")

    use_camera = st.checkbox("Use Camera")
    if use_camera:
        image = st.camera_input("Take a picture")
    else:
        image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    st.subheader("Enter data")
    name = st.text_input("Name")
    surname = st.text_input("Surname")
    age = st.number_input("Age", min_value=0, max_value=100)
    job_post = st.text_input("Job Post")
    access_level = st.number_input("Access Level", min_value=0, max_value=10)

    if st.button("Sign Up"):
        if image is not None:
            if use_camera:
                bytes_data = image.getvalue()
            else:
                bytes_data = image.read()

            encoded_image = base64.b64encode(bytes_data).decode("utf-8")

            info = PersonInfo(
                name=name,
                surname=surname,
                age=age,
                job_post=job_post,
                access_level=access_level,
            )

            data = {"photo": encoded_image, "info": info.json()}

            headers = {"Content-Type": "application/json"}
            response = requests.post(
                "http://127.0.0.1:8001/database/create_bytes",
                json=data,
                headers=headers,
            )

            # Обработка ответа от бэкенда
            if response.status_code == 200:
                json_data = response.json()

                # Получение значения поля client_id из JSON-ответа
                message = json_data["message"]

                # Отображение значения client_id в Streamlit
                st.success(message)
            else:
                st.error("Face recognition failed. Please try again.")
        else:
            st.warning("Please upload an image.")


def login():
    st.subheader("Log In")

    use_camera = st.checkbox("Use Camera")
    if use_camera:
        image = st.camera_input("Take a picture")
    else:
        image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if st.button("Recognize"):
        if image is not None:
            if use_camera:
                bytes_data = image.getvalue()
            else:
                bytes_data = image.read()

            encoded_image = base64.b64encode(bytes_data).decode("utf-8")

            data = {"photo": encoded_image}
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                "http://127.0.0.1:8001/model/recognize_bytes",
                json=data,
                headers=headers,
            )

            if response.status_code == 200:
                st.success("Face recognition successful!")

                text = response.text
                st.write(text)
            else:
                st.error("Face recognition failed. Please try again.")
        else:
            st.warning("Please upload an image.")


def main():
    st.title("Face Recognition Backend")

    choice = st.sidebar.radio("Выберите вкладку", ["Log In", "Sign Up"])

    if choice == "Log In":
        login()
    elif choice == "Sign Up":
        signup()


if __name__ == "__main__":
    main()
