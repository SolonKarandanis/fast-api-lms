from fastapi import FastAPI


app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Solon",
        "email": "skarandanis@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)



