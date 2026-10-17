# EU5 native dosyaları ile proje karşılaştırması

13 Ekim 2026 tarihinde kurulu oyunun dosyaları, çalışma alanındaki mod,
`et-history-data` ve dönüştürücü birlikte incelendi. **Aynı üç GPT-6 Luna
ajanı 89 alan/sistem karşılaştırması hazırladı.** Buna göre 12 yeni araştırma
kaydı toplandı; bunlardan biri MÖ 3000 sonrasını açıklayan karşılaştırma
kaydıdır. Native biçim örnekleri gerçek dosya ve satırlarıyla raporlandı.

En önemli sonuç: eksikler yalnız tarihsel bilgi eksikliği değildir. Şemada
bulunup dönüştürülmeyen alanlar, 1337 verisini koruyan dosyalar ve tarih
öncesi için henüz tasarlanmamış oyun karşılıkları da vardır. Dolayısıyla her
bulgunun hangi alanı besleyeceği ve mevcut akışın o alanı aktarıp aktarmadığı
araştırma görevinin parçası olmalıdır.

## Ayrıntılı raporlar

| İnceleme | Alan/sistem | Rapor | Makine tarafından okunabilir karşılaştırma |
|---|---:|---|---|
| Ülke, hükümet, kimlik, hanedan ve karakter | 30 | [countries-characters.md](countries-characters.md) | [countries-characters.yml](countries-characters.yml) |
| Lokasyon, nüfus, kaynak, yapı ve ağlar | 29 | [locations-population.md](locations-population.md) | [locations-population.yml](locations-population.yml) |
| Çağ, teknoloji, birimler, diplomasi ve diğer yöneticiler | 30 | [ages-systems.md](ages-systems.md) | [ages-systems.yml](ages-systems.yml) |

[inventory.yml](inventory.yml) dosya envanterini ve SHA-256 karşılaştırmasını,
[history-coverage.yml](history-coverage.yml) tarih kapsamı ölçümlerini,
[reference-cache-audit.yml](reference-cache-audit.yml) referans önbelleği
kontrolünü saklar. Dış kaynaklar her incelemenin `*-sources.yml` dosyasındadır.

## Kurulumun mevcut durumu

Native ve mod `main_menu/setup/start` klasörlerinde karşılaştırılan **25
dosyanın tamamı bulunuyor**. Mod dosyalarının altısı native ile byte düzeyinde
aynı: `14_development`, `21_locations`, `22_situations`, `24_town_rights`,
`25_area_preferences`, `26_ai_personalities`. Diğer 19 dosya farklıdır.
Farklılık tek başına doğruluk veya bozukluk göstermez.

Native `in_game/common` ve mod eklerinin birleşik envanteri 124 klasör
kategorisi içerir. Mod sekiz kategoride ek tanımlar taşır: kültür grupları,
kültürler, kutsal yer türleri, kutsal yerler, dil aileleri, diller, din grupları
ve dinler. Bir kategorinin modda ek dosyası bulunmaması o sistemin oyunda
eksik olduğu anlamına gelmez; native tanımlar ile modun kurulum durumları
ayrı katmanlardır.

Dönüştürücü altı kurulum dosyasını native kaynaktan kopyalar; diplomasi,
görüşler, rakipler, koloniler ve ordular için beş boş yönetici üretir.
`02_core` ve `13_religion` dosyaları elle tutulur. Dosya adlarından içerik
varsayılmamıştır: örneğin native `13_religion.txt` bir `building_manager`
ile başlar, `religion_manager` ise `02_core.txt` içindedir.

## Öncelikli farklar

| Alan | Native örnek/yapı | Bizdeki durum | Gereken iş |
|---|---|---|---|
| Tarihli lokasyon durumu | Setup dosyalarında lokasyon kimliklerine bağlı durumlar | MÖ 6000, 4000 ve 3100 kapsam kontrollerinde ülke/lokasyon durumları yok | Kaynaklı yer, evre, koordinat ve doğru harita eşlemesi |
| Nüfus | `define_pop` içinde tür, büyüklük, kültür ve din | YAML pop değerleri oran; toplam 1337 önbelleği × geçici dönem katsayısı | Tarihli toplam tahmin, birim, kapsam, yöntem ve belirsizlik |
| Yerleşim ölçeği | Lokasyon rank ve town setup tanımları | Mevcut 20.939 lokasyon dosyasında `city:` alanı bulunmadı; çıktı için rank ve setup birlikte aranıyor | Yerleşiklik, alan ve işlev kanıtı; muhafazakâr rank karşılığı |
| Kaynaklar | Goods tanımları ve ekonomik üretim yapıları | `resource` okunup doğrulanıyor; mevcut jeneratörler `loc.resource` yazmıyor | Önce kaynak/üretim anlamını netleştirmek, sonra aktarım desteği |
| Ülke/topluluk | Ülke tanımı ile setup durumu ayrı | Model yalnız sahip olduğu/kontrol ettiği lokasyon bulunan tagleri oluşturuyor; belgelenmiş `pop/building/army` türleri modelde taşınmıyor | Topluluk temsilini tasarlamak; siyasi sınır uydurmamak |
| Hükümet ve veraset | Preset include, hükümet, heir selection, ruler term | Preset ve mevcut hükümdar aktarılıyor; çok sayıda veraset/yasa/dil alanı taşınmıyor | Kaynak toplamanın yanında model/jeneratör desteği |
| Başkent | Lokasyon ID'si | Eksikse ilk sahip olunan lokasyon seçilebiliyor | Kaynaklı merkez ve doğrulanmış coğrafya; fallback'i tarihsel bilgi saymamak |
| Çağ | `common/age` içinde yıllar ve oyun etkileri | Altı araştırma sınıfı oyun çağlarını tanımlamıyor; çıktı sabit `age_1_traditions` | Takvim sınıfları ile oyun çağı tasarımını ayrı tutmak |
| Teknoloji | Advances, önkoşullar ve yaş/dönem kapıları | Her ülke sabit `starting_technology_level = 3` alıyor | Yerel kullanım ve yayılma kanıtı; ayrı teknoloji aktarımı |
| Kurumlar ve yasalar | Aktif kurumlar, doğum yerleri, reform/law tanımları | Elle tutulan kurum başlangıçları ve preset varsayımları var; tarihli yasa/reform akışı eksik | Neolitik faaliyeti feodal hukuk veya modern kurumla eşitlememek |
| Ticaret, yollar ve üretim | Markets, bağlantılar, production methods | Pazar/yol desteği sınırlı; üretim yöntemleri için tarihli alan yok | Provenans ve üretim yeri; güzergâh/çıktı miktarını ayrıca kaynaklamak |
| Savaş ve ordular | War manager, unit types ve unit manager | Savaş aktarımı kısmi; ordular boş | Tarihli olay ve katılımcı kanıtı; buluntudan ordu büyüklüğü üretmemek |

Bu tablo native dosyalarda **gözlenen biçimleri** ve mevcut kod davranışını
karşılaştırır. Native bir örnekte kullanılan alan, tek başına motorun her
senaryoda zorunlu tuttuğu alan değildir. Aynı şekilde yorum satırındaki
“vanilla rule” ifadesi motor davranışına ilişkin deneysel kanıt sayılmaz.

[validation.yml](validation.yml) kayıtlardaki kimlikleri, kaynak bağlarını,
aralıkları ve araştırma görevleriyle ilişkilerini kontrol eder; hata listesi
boştur. Bu kontrol oyun motorunun yükleme testi yerine geçmez.

## Ölçülen tarih kapsamı

3337 ülke, 20.939 lokasyon ve 1413 karakter dosyası okunabildi. Karakter
dosyaları toplam 31.240 karakter kimliği içeriyor. MÖ 6000, 4000 ve 3100
kontrollerinde bu üç grupta ilgili tarihe kadar gelen kayıt bulunmadı.
Bu üç tarih yalnız kapsam kontrolüdür; yeni başlangıç senaryosu seçimi değildir.

58.2.1 için mevcut kodun salt okunur dünya kurma işlemi 353 ülke, 20.939
lokasyon ve 229 yaşayan karakter üretti; 11.082 lokasyonda sahibi vardı.
Bu sayılar motor gereksinimi veya tarihsel doğruluk ölçüsü değildir. Dünya
modeli tarihsel durumu boş lokasyonlar için de nesne oluşturabilir; ülke
dosyalarındaki ad/renk gibi temel durumlar da gerçek siyasi varlık sayılmaz.

Önceki 77 araştırma kaydı `research/prehistoric` altında duruyor.
`build_world` bu klasörü okumuyor. Kaynaklı bilgi henüz konum, tarih ve
alan karşılığıyla oyun tarihine taşınmış değildir. Önbelleğin mevcut native
ve moddan aynı referans çıkarıcıyla yeniden okunması fark göstermedi;
çıkarıcının basit regex kullanması bütün ID türlerinin doğrulandığı anlamına gelmez.

## Buna göre başlayan araştırma

- [Ülke/karakter kayıtları](countries-characters-research.yml): üç akrabalık ve
  defin bulgusu. Hane ilişkileri veya anne hattı sonuçları adlı hanedan,
  hükümdar ya da veraset yasası olarak kaydedilmedi.
- [Lokasyon/nüfus kayıtları](locations-population-research.yml): beş kayıt;
  nüfus modelinin aralığı, besin ekonomisi, obsidyen provenansı, örneklem
  bilgisi ve yayınlanmış koordinat. Bir kazı noktasının nüfusu bütün oyun
  lokasyonunun nüfusu olarak kullanılmadı.
- [Teknoloji/çatışma kayıtları](ages-systems-research.yml): dört kayıt;
  metal nesneler, Hamoukar'daki savaş yorumu ve üretim bulguları; Standard of
  Ur ise sonraki dönem karşılaştırmasıdır.

Araştırma görevleri ve kabul koşulları
[research-plan.yml](research-plan.yml) içinde önceliklendirildi. Yeni veri
bir site/evreye, kaynak iddiasına, belirsiz tarihe, coğrafi ölçeğe ve hedef
alanın anlamına bağlanacak. Kaynak olmayan hükümdar adları, ordu sayıları,
etnik sınırlar veya din oranları tamamlanmış değer gibi doldurulmayacak.

## Açık teknik sınırlar

Modun date window değeri 58.2.1–9999.12.31, native değer 1337.4.1–1836.12.31.
Dönüştürücünün negatif yıl ayrıştırması motorun MÖ tarih yükleme, gösterme
ve ilerletme davranışını doğrulamaz. Bunlar ayrı çalışma ve yükleme testleri
gerektirir. Araştırma arşivi bu doğrulama beklenirken kaynak tarihlerini koruyabilir.

Kurulum klasörünün adı patch sürümünü güvenilir biçimde belirlemiyor.
Son log aynı native yolu gösteriyor; yerel manifest adı ve exe'nin genel
1.0 sürüm kaynağı ayrıntılı patch doğrulaması sağlamıyor. Bu rapor internetteki
başka bir sürümün yerine **incelenen kurulu dosyaları** esas alır.

Bu turda değişiklikler araştırma ve rapor dosyalarıyla sınırlıdır. Native,
mod, dönüştürücü ve mevcut tarih dosyaları karşılaştırma için okundu.
