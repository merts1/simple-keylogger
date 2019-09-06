# simple-keylogger
Belirli bir süre çalışan ve kaydettiği veriyi bir google form adresine submit eden, ardından txt dosyasını ve kendini silen basit bir keylogger script.

Bir adet .pyw uzantılı bir adet de .py uzantılı dosya bulunmakta. Bunlardan .pyw uzantılı olan çalıştırıldığı anda arka planda kullanıcıya görünmeden klavye tuş bilgilerini bir text dosyası oluşturup yazdırıyor. Dosya herhangi bir konumdan çalıştırılabileceği için masaüstünde olmaması kullanıcının fark etmemesi için yeterli. Ancak yine de görev yöneticisinde işlemler menüsünde python olarak gözükür.

NOT: İki dosyanın da çalışması için "pynput" kütüphanesi indirilmelidir.

İkinci dosya içerisinde ayarlanmış süre boyunca çalıştırıldığı andan itibaren klavye tuş bilgisi toplayıp bunu yine bir txt dosyasına yazar. Diğer dosyadan farkı ise, topladığı bilgiyi seçili google formuna online olarak submit eder ve hem txt dosyasını hem de kendini siler. Yani ikinci script self-descructive olduğundan, belirli bir süre çalışıp hiç iz bırakmadan veriyi istenilen adrese yükler.

Dosya içerisinde değiştirilmesi gereken yerler script içerisinde belirtilmiştir.
