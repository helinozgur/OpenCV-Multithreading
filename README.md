# OpenCV-Multithreading
OpenCV Multithreading konsunu anlattığım medium yazıma [buradan](https://helinozgur.medium.com/opencvde-%C3%A7oklu-i%CC%87%C5%9F-par%C3%A7ac%C4%B1klar%C4%B1-multithreads-ile-kodun-%C3%A7al%C4%B1%C5%9Fmas%C4%B1n%C4%B1-h%C4%B1zland%C4%B1rma-83aed171f496) ulaşabilirsiniz.
## Thread Nedir?
İş parçacıkları(Threads) kısaca bir dizi talimatlardan oluşan akışlardır. Bunlar işletim sistemi tarafından çalıştırılmak üzere programlanabilir ve birden çok çekirdekte paralel olarak veya tek bir çekirdekte aynı anda çalıştırılabilir.
![image](https://user-images.githubusercontent.com/52162324/135287594-40aeeb2a-fedf-4a4a-8812-b79c084b34d7.png)
[1]

## Python İş Parçacığı(Threading) Modülü
Python’da iş parçacıkları Python’ın kendi modülü olan threading modülü tarafından oluşturulmaktadır. Modüle [link](https://docs.python.org/3/library/threading.html) üzerinden erişebilirsiniz.


## Kodlar Hakkında
Kod örneklerimizde 1920x1080 çözünürlüğe sahip 10 saniyelik aşağıdaki gifteki gibi bir video kullanacağız.Multithread mantığını anlamak istiyorsanız öncelikle iş parçacığı olmadan kodunuzun çalışma hızına bakınız([thread_yok_findik.py](https://github.com/helinozgur/OpenCV-Multithreading/blob/main/thread_yok_findik.py)). Ardından kodu 3 farklı iş parçacığına böleceğiz bu iş parçacıklarından birincisi dosyadan videoyu okuyacak, ikincisi okunan videoya bulanıklaştırma işlemi yapacak ve üçüncü iş parçacığı ise bulanıklaştırma işlemi yapılan görüntüyü OpenCV fonksiyonu yardımı ile ekrana yansıtacak([thread_video_findik.py](https://github.com/helinozgur/OpenCV-Multithreading/blob/main/thread_video_findik.py)). Bu yöntemle görüntünün işlenme süresi iş parçacığı içermeyen halinden daha hızlı çalıştığını gözlemleyebilirsiniz.

![image](https://user-images.githubusercontent.com/52162324/135288221-315af210-dda4-430f-8964-74c37aa6ad37.png)

