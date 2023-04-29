# Gereklilikler

- Bir AWS Bulut Hesabı

Hesap oluşturmak için [bu](https://portal.aws.amazon.com/billing/signup#/start/email) adrese gidip, bilgilerinizi girebilirsiniz.
Hesabı oluştururken bir adet kredi kartı, sanal kart veya banka kartı isteyecektir. İçinde 1-3 dolar arası bir para bulunan bir sanal kart tanımlamanız yeterli olacaktır(Ininal veya Papara büyük olasılıkla çalışıyordur).


- Herhangi bir IDE

Spesifik olarak bu workshop için ihtiyacınız olmasa da, bir adet kodlama ortamı hayatınız kolaylaştıracaktır. Bizim önerimiz VSCode.

- Python v3.9+

Bu workshopta kodlamalarımızı Python ile yapacağız, referans demomuz da Python ile yazıldı.

- Bir adet 2FA'e sahip Gmail hesabı.

Workshop'un referans demosu, google'ın mail servislerini kullanıyor. Farklı mail sağlayıcıları için, farklı sunucu adresleri ve portlar bulunmakta, farklı güvenlik protokolleri bulunmakta. 2FA, uygulama şifresi almanız için zorunlu bir durum.


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
Daha detaylı bilgi için, [bu](https://aws.amazon.com/tr/lambda/serverless-architectures-learn-more/) linkten whitepaper'ı indirebilirsiniz.

# Aşamalar

## Aşama 1: Bir lambda fonksiyonu oluşturmak.

- [AWS](https://aws.amazon.com/tr/) hesabınıza giriş yapın. Yukarıda bulunan arama kutucuğuna "Lambda" yazarak, lambda fonksiyonlarınızın olduğu bir konsola ulaşacaksınız.

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

```python
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
```

Bunu fırsat bilerek, lambda konusunda bir konuya açıklık getirmek istiyorum. Lambda, temelde bir API gibi çalışır, yani bir istek attığınızda, size bir cevap verir.
Bu durumda; test butonuna tıkladığınızda veyahut bir şekilde fonksiyonu tetiklediğinizde, standart bir IDE'den farklı olarak, hata mesajları veya sonuçların aksine, sadece bir 'statusCode' ve bir 'body' döndürür. Uygulamanın çalışma sırasında çıkardığı logları(günlüğü), Cloudwatch Logs üzerinden görebilirsiniz. Bu loglara erişmenin en kolay yolu, lambda fonksiyonunuzun konsolunda, "Code", "Test"... şeklinde giden menüde Monitor'a tıklayıp, "Cloudwatch Logs"'a tıklamaktır. Çıkan sayfada, uygulamanızın bütün çalıştığı zamanda konsola verdiği veya gizli olarak tuttuğu logları görebilirsiniz.

- Hazır olan kod ile ilk testimizi yapmak için, Testing menüsüne gelin. Test ismi kısmını doldurun.

AWS Lambda, tetikleyici ile ilgili bilgileri event objesi ile alır, bu durumda tetikleyicimiz Lambda'nın "Test" modülü, ve test event'imizin içeriğini de, aşağıdaki JSON kısmını doldurarak yapabiliyoruz. Şu anlık bir değişiklik yapmadan Test'e tıklayın.

Bu işlemin sonucunda, "Execution result: succeeded" almalısınız.

Tebrikler, artık çalışan bir lambda fonksiyonuna sahipsiniz.

## Ekstra Aşama: Lambda fonksiyonunu otomatik tetikleme

Bu aşama zorunlu değil, ama ben göstermek istediğim için göstereceğim. Öncelikle biraz ön bilgi ile başlayalım.

AWS Lambda, yukarda bahsettiğmiz üzere bir "API" mantığında çalışıyor. Buna dayanarak şunu söyleyebiliriz: fonksiyonu her zaman tetikleyen(trigger) bir eylem olmalı ve bu eyleme geri dönen bir sonuç olmalı. Bu eylem API Gateway aracılığı ile gelen HTTP isteği, veya cloudwatch events(AWS'nin zaman ayarlı tetikleyicisi) ile gelen istekler olabilir. Bu isteklerin kendilerine has bir yapısı vardır ve bu isteklere, AWS Lambda'nın bir cevap göndermesi gerekir. Eğer bir "return" komutu eklenmezse, sizin ayarlarınızda belirlediğiniz zaman aşımına uğrayana kadar çalışacaktır.

Bu aşamada, tetikleyicilerin en kolayı olan cloudwatch events'i göstereceğim.

- AWS konsolunun arama kutucuğuna, cloudwatch yazın.
- Solda bir menünüzün olması gerek, "Events" sekmesi altında "Rules" butonuna tıklayın.
- Gelen sayfada, Create rule'a tıklayın. Event source bölümünün altında, "Schedule" kutucuğunu işaretleyin.

Burada, 2 farklı şekilde ayarlama yapabilirsiniz. Genel olarak bütün sistemlerde kullanılabilen "cron expressions" ile, veya üstte kendiniz kutucukla seçerek. Cron expressions hakkında daha çok şey öğrenmnek için [bu]() linke tıklayabilirsiniz. Benim de tavsiyem cron expressions kullanmanızdır.

- Sağ tarafta Add target'e tıklayın. Lambda fonksiyonunuzu seçin. İşlemleriniz bittikten sonra "Configure Details" ile sonraki sayfaya geçip, kuralınızın ismini ve açıklamasını yazarak oluşturma işlemini tamamlayabilirsiniz.


Artık, belirlediğiniz sürede sürekli olarak lambda fonksiyonunuz otomatik bir şekilde tetiklenecek.

## Aşama 3: Gerçek bir uygulama.

Bu aşamada, size gerçek bir uygulama örneği göstereceğiz. Bizim seçtiğimiz uygulama, otomatik mail modülü.

Bu workshop'un klasöründe, app.py adında bir uygulama bulunmakta. Kodun içeriği büyük ölçüde dökümente edilmiş ve anlatılmış durumdadır. Daha detaylı bilgi için interneti araştırabilirsiniz, bol bol kaynak mevcut. 
- Bu uygulamanın kaynak kodunun tamamını kopyalayıp, lambda fonksiyonunda IDE kısmına yapıştırın.
- Kaynak kodunu inceleyin, boş bırakılmış ve sizin bilgileriniz ile doldurulması gereken kısımları doldurun.(Email ve uygulama şifresi olmak üzere.)
- İşlemleriniz bittiği zaman, test etme zamanı geldi.

Az önceki test ekranına dönün, test eventinizin json formatında olması gerekmekte.
Örnek bir json dosyası, aşağıda mevcut.
```json

{
  "mailSubject": "Test Mail",
  "mailContents": "TestMail",
  "mailList": "ulworddev@gmail.com"
}

```

Mailcontents aslında bir html girdisi. Oraya eğer ki bir HTML girdisi girerseniz, Sonuç olarak gelen mailiniz html çıktısı şeklinde gözükecektir.

## Ekstra: Şimdi ne yapmalı?

AWS çok büyük bir ekosisteme sahip. Bu ekosistemdeki bütün araçları kullanmak imkansıza yakın olsa da, nereden devam edebileceğiniz konusunda yol gösterebiliriz.

Eğer ki lambda fonksiyonları ve sunucusuz sistemler üzerine çalışmaya devam edecekseniz, API Gateway üzerine çalışarak, API servisleri hakkında araştırmalar yapabilirsiniz. API gateway, şahsen benim en önemli gördüğüm araçlardan bir tanesi.

Eğer ki web sitesi ayağa kaldırma, yürürlükte tutma gibi konular üzerine çalışmak istiyorsanız; Elastic Beanstalk servisine göz atabilirsiniz. Otomize katlanabilirlik, load balancing gibi özelliklere sahip. Hayatınızı kolaylaştıracaktır.

Eğer ki data ve obje tutma konuları üzerinde servislere ihtiyacınız varsa; data için DynamoDB, objeler için S3 Bucket servislerini araştırabilirsiniz.

## Kritik Konu: Faturalandırmalar ve Ücret ödeme

AWS, oldukça fazla miktarda servise ev sahipliği yapıyor. Ancak bütün servisler belli bir ücret alıyor. Örneğin bir NAT ağı oluşturmanız ve unutmanız durumunda, aylık 50 dolar'a varacak ücretler ödemeniz istenebilir. Eğer ki bir üründe kullanmayıp unuttuğunuz bir servis var ise, amazon desteğe yazmanız durumunda "Good will refund" dedikleri iade işlemini gerçekleştireceklerdir. Eğer ki hesabınızdan para çekilemeyecek durumdaysa(banka kartı veya sanal kart durumunda), belli bir süre para çekilememsinin ardından hesabınız kapatılacaktır. Aklınızda bulunsun.

Bir şeyleri unutma konusunda herkesin bir anısı vardır. Bu konuda canınızı sıkmayın. Bana da farklı bir bulut sağlayıcısında 150 dolarlık fatura kesildi, desteğe yazdığınızda çözüyorlar.

# Son Söz

Bulut teknolojileri büyük teknolojiler ve öğrenecek çok şey var. İnternet çağındayız, her konuda bilgiye ulaşmak çok kolay. Bu özellikle bulut sistemleri ve AWS için geçerli. Okumaktan, araştırmaktan vazgeçmeyin!


# Bana ulaşmak için;

Maillerime sürekli bakıyorum, bunun dışında linkedin'den de ulaşabilirsiniz.

Mail: candogann02@gmail.com

Linkedin: linkedin.com/in/ali-can-dogan/

