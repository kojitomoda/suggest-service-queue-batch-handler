FROM public.ecr.aws/lambda/python:3.12-x86_64 AS build

# 必要なライブラリをインストール
COPY requirements.txt ./
RUN pip install -r requirements.txt --target .

FROM public.ecr.aws/lambda/python:3.12-x86_64
ENV HOME="/tmp"

# 必要なパッケージをインストール
RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm tar

# Pythonライブラリをコピー
COPY --from=build /var/task /var/task

# アプリケーションコードをコピー
COPY app/ ./app/

# Lambda関数のエントリーポイント
CMD ["app.main.lambda_handler"]