# Bilgisayar Kamerası ile Fare Kontrolü

Bu proje, bilgisayar kamerası yardımıyla el hareketleriyle fareyi kontrol etmeye olanak tanır. Python'da OpenCV ve MediaPipe kütüphaneleri kullanılarak el izleme yapılır ve işaret parmağı ile fare imleci ekranda hareket ettirilir. İşaret ve orta parmağınızı birleştirerek fare tıklaması gerçekleştirebilirsiniz.

## Gerekli Kütüphaneler

Projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

- `opencv-python`
- `mediapipe`
- `pyautogui`
- `math`

### Kütüphanelerin Yüklenmesi

Gerekli kütüphaneleri yüklemek için terminal veya komut satırında aşağıdaki komutları çalıştırın:

```bash
pip install opencv-python mediapipe pyautogui```

## Proje Yapısı

- `index_finger_tip`: İşaret parmağı ucunun kamera tarafından tespit edilen koordinatları.
- `middle_finger_tip`: Orta parmak ucunun kamera tarafından tespit edilen koordinatları.
- `pyautogui.moveTo(screen_x, screen_y)`: Fare imlecini, işaret parmağı koordinatlarına göre hareket ettirir.
- `pyautogui.click()`: İşaret ve orta parmak birleştiğinde fare tıklamasını gerçekleştirir.

## Çalıştırma

1. Python ortamınızda projeyi çalıştırın:

    ```bash
    python mouse_control.py
    ```

2. Bilgisayar kamerası açılacaktır ve işaret parmağınızı hareket ettirerek fareyi kontrol edebilirsiniz.
3. İşaret parmağı ile orta parmağı birleştirerek tıklama gerçekleştirebilirsiniz.
4. `q` tuşuna basarak uygulamayı kapatabilirsiniz.

## Fonksiyonlar

### `calculate_distance(point1, point2, frame_width, frame_height)`

Bu fonksiyon, iki parmak arasındaki piksel mesafesini hesaplar. Eğer mesafe belli bir eşik değerden küçükse (örneğin 40 piksel), tıklama işlemi başlatılır.

## Gereksinimler

- Bir bilgisayar kamerası
- Python 3.x

## Özellikler

- Gerçek zamanlı el izleme
- Fare imleci hareketi işaret parmağı ile kontrol edilir
- İşaret ve orta parmak birleştiğinde fare tıklaması gerçekleştirilir
