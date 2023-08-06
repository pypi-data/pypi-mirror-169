FROM balenalib/raspberrypi4-64-debian

ENV UDEV=on

RUN mkdir /app
RUN mkdir /out

RUN apt update && apt install -y wget gnupg2
RUN echo "\ndeb http://deb.debian.org/debian bullseye main contrib non-free\ndeb http://security.debian.org/debian-security bullseye-security main contrib non-free\ndeb http://deb.debian.org/debian bullseye-updates main contrib non-free" >> /etc/apt/sources.list.d/raspi.list
RUN wget https://archive.raspbian.org/raspbian.public.key && apt-key add raspbian.public.key

RUN apt update && apt install -y \
    python3 \
    python3-libcamera \
    python3-picamera2 \
    python3-kms++ \
    ffmpeg \
    python3-pyqt5 \
    python3-prctl \
    libatlas-base-dev \
    python3-dev \
    python3-pip \
    libcamera0 \
    libcamera-dev \
    libcamera-apps-lite \
    v4l-utils \
    gcc-aarch64-linux-gnu
RUN pip3 install numpy --upgrade


COPY ./capture/requirements.txt requirements.txt
RUN READTHEDOCS=True pip install -r requirements.txt

WORKDIR /app

COPY ./capture/ /app/capture
COPY ./run_capture.py /app/run_capture.py
COPY ./run_upload.py /app/run_upload.py

CMD ["python3", "run_capture.py"]
