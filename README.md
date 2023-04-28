# Gereklilikler

- Bir AWS Bulut Hesabı

Hesap oluşturmak için https://portal.aws.amazon.com/billing/signup#/start/email adresine gidip, bilgilerinizi girebilirsiniz.
Hesabı oluştururken bir adet kredi kartı, sanal kart veya banka kartı isteyecektir. İçinde 1-3 dolar arası bir para bulunan bir sanal kart tanımlamanız yeterli olacaktır(Ininal veya Papara büyük olasılıkla çalışıyordur).


- Herhangi bir IDE

Spesifik olarak bu workshop için ihtiyacınız olmasa da, bir adet kodlama ortamı hayatınız kolaylaştıracaktır. Bizim önerimiz VSCode.

- Python v3.9+

Bu workshopta kodlamalarımızı Python ile yapacağız, referans demomuz da Python ile yazıldı.

- Bir adet Gmail hesabı.

Workshop'un referans demosu, google'ın mail servislerini kullanıyor. Farklı mail sağlayıcıları için, farklı sunucu adresleri ve portlar bulunmakta, farklı güvenlik protokolleri bulunmakta.


# Ön Bilgi: 

Bu metinin en altında, ingilizce anahtar kelimeler bulunmakta. Bu anahtar kelimeleri internet üzerinden "what is **" şeklinde aratırsanız, genel olarak bu repoda ve workshopta anlatılan konular hakkında çok daha detaylı bilgiye ulaşabilirsiniz. 

## Bulut Sistemleri, On-Prem Sistemler ve Sunucusuz Sistemler

Keywords: "Serverless Architecture", "on-prem systems", "cloud services".

Eskiden neredeyse her şey, fiziksel olarak bakılması ve sürdürülmesi gereken fiziksel sunuculara bağlıydı. Neredeyse her şirket, kendi içinde sunucular almak ve bunlar için ortam, insan gücü ve zaman harcaması gerekiyordu.
Son zamanlarda, artık bulut sistemlerine geçilmeye başlandı. Hala on-premise sunucular(Kurum içi sunucular, on-prem diye bahsedeceğiz.) kullanılsa da, artık çoğu zaman AWS gibi bulut servisi sağlayıcılarına yöneliyoruz.
Bulut servisi sağlayıcılarının bize sağladığı onlarca servis var, bunlardan birisi ve bizimde en çok kullandığımız "sunucusuz" diyebileceğimiz, neredeyse hiçbir ortam bakımına ihtiyaç duymayan sistemler.
Hemen hemen bütün sağlayıcılarda bir adet sunucusuz kod çalıştırmak için servis var. AWS'de Lambda, Azure'da Functions gibi.
Bu workshopta, size bulut sistemlerinin ve sunucusuz sistemlerin nasıl çalıştığını göstereceğiz. Dikkat edilmesi gereken hususlar hakkında da bilgilendirmeler yapacağız.



## Sunucusuz Sistemler Nedir

Keywords: "Serverless Architecture"

Sunucusuz(Serverless) sistemler/mimari, herhangi bir alt yapı yönetmek zorunda olmadan(donanımsal ve genellikle yazılımsal), uygulamaları ve kodları çalıştırabildiğimiz yapılardır. Sunucusuz desek dahi, teknik olarak hala bir sunucu altyapısı ile çalışıyor, ancak bizim yönetmemizi gerektiren hiçbir şey yok. Her şey servis sağlayıcısı tarafından otomatik ve sistematik bir şekilde yönetiliyor.
Sunucusuz mimari ile uygulamaları, alt yapıyı dert etmeden geliştirebiliyoruz. Tabii yine bize getirilen bazı kısıtlamalar olabiliyor, ancak bütün yapılar kısıtlamalara sahiptir. Genel olarak bu kısıtlamalar ve faydaları karşılaştırıp en iyi yapıları bulmak ve kurmak, geliştirmenin en önemli parçası denilebilir.
Daha detaylı bilgi için, https://aws.amazon.com/tr/lambda/serverless-architectures-learn-more/ linkinden whitepaper'ı indirebilirsiniz.

# Aşamalar

## Aşama 1: Bir lambda fonksiyonu oluşturmak.

- AWS[https://aws.amazon.com/tr/] hesabınıza giriş yapın. Yukarıda bulunan arama kutucuğuna "Lambda" yazarak, lambda fonksiyonlarınızın olduğu bir konsola ulaşacaksınız.

- Konsolda, "Create Function" butonuna tıklayın.
