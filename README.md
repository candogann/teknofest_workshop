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

Burada 3 farklı yol ile fonksiyon oluştabileceğinizi göreceksiniz. 
Birinci yol "Author from Scratch", yani sıfırdan oluşturma. Bütün her şeyi sizin ayarladığınız, tamamen sizin kontrolünüzde olan bir oluşturma biçimi.
İkinci yol "Use a Blueprint", yani önceden hazır edilmiş belli başlı ön ayarlarla birlikte kurma. Burada belli ayarlar otomatik yapılmış olarak gelir.
Üçüncü yol ise bir container ile oluşturma. Bu yol, üçü arasında en karmaşık olanı denilebilir. Çok katmanlıdır, ama getirdiği faydalar uygulama geliştirmenizde inanılmaz fayda sağlar. Benim de şahsen tercih ettiğim yoldur.

Biz bu workshop için birinci yoldan gideceğiz.

- "Author from Scratch" seçili iken, aşağıda bulunan kısımları doldurun.

Runtime olarak Python 3.9 veya üstü bir sürüm seçmelisiniz.
Architecture olarak x86_64 veya arm64 arasında bu uygulama bazında fark olmamalı, ancak biz x86 seçtik.
"Permissions" kısmına dokunmanıza gerek yok, ancak eğer ki AWS üzerine çalışmaya devam etmeyi düşünüyorsanız, IAM rolleri nedir öğrenmelisiniz. Bu workshopta girmeyeceğiz.

Advanced settings'te, şimdilik dokunmamızı gerektiren bir durum yok. Create function butonuna basarak, fonksiyonunuzu oluşturabilirsiniz.

## Aşama 2: Hello world!

- Lambda fonksiyonumuzu oluşturduk, eğer ki yukardaki adımları izlediyseniz, lambda sizin için otomatik bir "Hello from Lambda!" döndüren bir fonksiyon oluşturdu.

Fonksiyonunuzun kodu, şu şekilde olmalı:

`
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
`

Bunu fırsat bilerek, lambda konusunda bir konuya açıklık getirmek istiyorum. Lambda, temelde bir API gibi çalışır, yani bir istek attığınızda, size bir cevap verir.
Bu durumda; test butonuna tıkladığınızda veyahut bir şekilde fonksiyonu tetiklediğinizde, standart bir IDE'den farklı olarak, hata mesajları veya sonuçların aksine, sadece bir 'statusCode' ve bir 'body' döndürür. Uygulamanın çalışma sırasında çıkardığı logları(günlüğü), Cloudwatch Logs üzerinden görebilirsiniz. Bu loglara erişmenin en kolay yolu, lambda fonksiyonunuzun konsolunda, "Code", "Test"... şeklinde giden menüde Monitor'a tıklayıp, "Cloudwatch Logs"'a tıklamaktır. Çıkan sayfada, uygulamanızın bütün çalıştığı zamanda konsola verdiği veya gizli olarak tuttuğu logları görebilirsiniz.

- Hazır olan kod ile ilk testimizi yapmak için, Testing menüsüne gelin. Test ismi kısmını doldurun. 


