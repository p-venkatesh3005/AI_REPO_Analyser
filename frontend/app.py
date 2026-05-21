import streamlit as st
import requests
import os


BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8001")


st.set_page_config(
    page_title="Repo AI Explainer"
)

st.title(
    "🧠 Repo AI Explainer"
)


# ==================
# UPLOAD
# ==================

uploaded_file = st.file_uploader(
    "Upload ZIP",
    type=["zip"]
)


if uploaded_file:

    if st.button(
        "Index Repository"
    ):

        try:

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/zip"
                )
            }

            response = (
                requests.post(
                    f"{BACKEND_URL}/upload",
                    files=files
                )
            )

            if (
                response.status_code
                == 200
            ):

                st.success(
                    response.json()[
                        "message"
                    ]
                )

            else:

                st.error(
                    response.text
                )

        except Exception as e:

            st.error(
                str(e)
            )


# ==================
# ASK
# ==================

st.divider()

question = st.text_input(
    "Question"
)


if st.button(
    "Ask"
):

    try:

        payload = {
            "question":
            question
        }

        response = (
            requests.post(
                f"{BACKEND_URL}/ask",
                json=payload
            )
        )

        st.write(
            "Status:",
            response.status_code
        )

        st.write(
            "Raw Response:"
        )

        st.code(
            response.text
        )

        if (
            response.status_code
            == 200
        ):

            data = (
                response.json()
            )

            st.subheader(
                "Answer"
            )

            st.write(
                data[
                    "answer"
                ]
            )

    except Exception as e:

        st.error(
            str(e)
        )