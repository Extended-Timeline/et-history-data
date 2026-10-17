# Tarihsel durumlar ve değişim süreçleri

Bu paket, oyunun kurulu native dosyalarındaki veri türlerini tarih araştırmasının sorularına çevirir. Modun hangi alanı bugün okuyabildiği araştırma kapsamını belirlemez. Native tanımlar da tarihsel doğruluğun kaynağı değildir: alanları native dosyadan, alanların tarihsel içeriğini kaynaklardan alırız.

Araştırma takvimi `periods/universal.yml` içindeki altı sınıftır. İlk ayrıntılı toplama hedefi tarih öncesinin tamamıdır. Bir sürecin kaynakta verilen aralığı -3000 sınırını aşıyorsa kesilmez; hangi kısmının dönem dışında kaldığı ayrıca belirtilir. Aynı takvim diliminde farklı bölgelerde farklı toplumsal biçimler bulunabilir.

## Her başlık için iki tür bilgi

**Durum kaydı:** Belirli bir yer ve zaman aralığında kimler yaşıyordu, hangi yerleşmeler ve siyasi yapılar vardı, ne üretiliyordu, hangi uygulamalar belgeleniyor? Yerleşme, bölge, topluluk ve devlet ölçekleri ayrı tutulur. Bir bulgunun kazıldığı nokta, o uygulamanın bütün bölgedeki yayılımı değildir.

**Süreç kaydı:** Önceki ve sonraki durum arasındaki değişim nerede, hangi aralıkta, hangi kanıtla görülüyor? Göç, yerel benimseme, siyasi bütünleşme, dil değişimi, ticaret, iklim veya çatışma açıklamalarının hangisi doğrudan destekleniyor; hangisi yazarın önerisi? Bir başlangıç ve sonuç bilmek, aradaki sebebi bildiğimiz anlamına gelmez.

Kayıtlar gerektiğinde birden çok başlangıç ve sonuç içerir. Bir topluluk bölünebilir, farklı topluluklar birleşebilir; bir dil başka bir siyasi kimlik içinde yaşamaya devam edebilir. Bir kültürün tek çizgi halinde sonraki kültüre dönüşmesi zorunlu değildir.

## Kanıtı oyun kuralına dönüştürmeden saklamak

Üç katman ayrı tutulur:

1. **Gözlem:** Tarihlenmiş buluntu, yazılı ifade, biyolojik örnek, yerleşme dizisi veya sayım.
2. **Tarihsel yorum:** Gözlemlerden çıkarılan göç, uzmanlaşma, otorite, temas veya değişim açıklaması; karşı görüşü ve belirsizliğiyle.
3. **Oyun tasarımı:** Bir teknolojinin maliyeti, kültür değişiminin hızı, bonus veya olay tetikleyicisi. Araştırma dosyasına tarihsel gerçekmiş gibi yazılmaz.

Örneğin bir bölgede tarım ve büyük yerleşmelerin birlikte görülmesi, tarımın her durumda devlet kurduğu sonucunu vermez. Araştırmanın desteklediği ilişki, olası koşullar ve karşı örnekler saklanır. Gelecekteki mekanik bu kanıtı kullanabilir; evrensel zorunlu koşul üretmek ayrı bir tasarım kararıdır.

## Kimlik alanları

Halkın kendi adı, dışarıdan verilen ad, arkeolojik kültür etiketi, konuşulan dil, siyasi aidiyet ve biyolojik soy bilgisi ayrı alanlardır. Bunlar arasında bağlantı kurulacaksa bağlantının da kaynağı gerekir. Çanak çömlek dağılımı tek başına dil haritası; genetik karışım tek başına etnik kimlik; hükümdarın dini tek başına bütün nüfusun dini değildir.

Native `in_game/common/cultures/00_cultures.info` satır 2 ve 22–26 dil ve birden fazla kültür grubu bağlantısını tarif eder. `ethnicities/00_ethnicities_african_bantu.txt` satır 1–31 genler, görünüş şablonu, ten, göz ve saç seçeneklerini içerir. Tarihsel halk kataloğu bu görünüş şablonlarına indirgenmez.

Ölçek ayrımı native veride de görünür: `main_menu/setup/start/06_pops.txt` satır 3–10 aynı yerleşmede farklı kültürlere sahip pop kayıtları tanımlar. `in_game/events/DHE/flavor_zaz.txt` satır 95–116 ülke kapsamındaki kültür/din değişimini; `in_game/events/debug/000_johan_debug.txt` satır 493–497 ise pop kapsamındaki değişimi örnekler. Debug örneği yalnızca alanların ayrıldığına kanıttır, tarihsel olay kanıtı değildir.

## Kayıt sözleşmesi

Mevcut `entity`, `subject`, `finding`, `dating`, `source_refs`, `confidence`, `integration` alanları korunur. Bir bulgu süreç hakkında ise aşağıdaki ek bilgiler kaynakta mevcut olduğu ölçüde tutulur:

| Bilgi | Saklanacak içerik |
|---|---|
| Kapsam | Bölge/site listesi, nokta veya alan, incelenen örneklem ve genelleme sınırı |
| Önceki/sonraki durum | Her durumun kendi tarih aralığı ve kanıtı; bilinmeyen taraf açıkça belirtilir |
| Değişim biçimi | Benimseme, süreklilik, ayrışma, birleşme, yer değiştirme, çöküş, yayılma veya tartışmalı değişim |
| Mekanizma | Kaynakta önerilen veya gösterilen açıklama; araştırmacının hipotezi ile doğrudan gözlem ayrı |
| Alternatifler | Rakip açıklamalar, örneklem veya tarihleme sınırlamaları |
| Bağlantılar | Bir gereksinim ID'si ve ilişkili bulgular; sonradan doğrulanacak kimlik ilişkileri |
| Kullanım | `collected`; tarihsel bulgu otomatik olarak oyun geçişi anlamına gelmez |

Ek alanlar bu araştırma paketine aittir; mevcut dönüştürücünün bunları işlediği iddia edilmez. Her cümlenin dayanağı `source_refs` içindeki bölüm, şekil, tablo veya veri kümesiyle takip edilebilir olmalıdır. Aynı kaynak birden çok iddiayı destekliyorsa hangi bölümün hangi iddiaya dayanak olduğu belirtilir.

Tarih aralıkları kaynakta bildirilen kesinliği korur. BCE, kalibre BP, kalibre edilmemiş radyokarbon yaşı ve referans yılı belirtilmeyen “years ago” aynı ölçek değildir. Kazı veya yayın yılı olay yılı değildir. Belirsiz aralık için kesin gün icat edilmez. Nüfus tahmininde birim, alan, yöntem ve hata aralığı; sayısal demografik oranlarda örneklem ve payda tutulur.

## Eksik veri nasıl işaretlenir?

**Başlangıç kanıtı var:** Bir veya birkaç kaynaklı bulgu mevcut; bölgenin ve dönemin tamamı araştırılmış değildir.

**Süreç eksik:** Başlangıç/sonuç hakkında bilgi var, aradaki değişim ve açıklamalar yeterince incelenmemiş.

**Kapsama eksik:** Bazı bölgeler veya tarih aralıkları açık kalmış.

**Katalogda bulunmadı:** Bu denetimde incelenen araştırma dosyalarında karşılık bulunamadı; tarihte bulunmadığı anlamına gelmez.

**Kanıt erişimi sınırlı:** Yayın özeti veya kurum özeti okunabildi; asıl veri/ekler henüz denetlenmedi.

**İncelenmedi:** İlgili dosya veya bilimsel literatür henüz denetlenmedi. Bu durum “yok” diye raporlanmaz.

## Bir bölgesel paketin tamamlanma koşulu

Bir yerleşme listesi tek başına yeterli değildir. Paket; araştırılan bölgeyi ve tarih aralığını tanımlar, bu katalogdaki her ilgili başlığı değerlendirir, kaynaklı durum kayıtlarını ve önemli değişim süreçlerini sunar. Uygulanamayan alanın neden uygulanamadığını, kanıt bulunmayan alanın ne kadar arandığını, tartışmalı alanın alternatiflerini kaydeder. Tarih öncesi için adlandırılmış hükümdar, hanedan veya din bilinmiyorsa bilinmeyen bırakılır.

Altı takvim sınıfını aynı alanlarla araştırabiliriz; her sınıfa aynı devlet, hukuk, sınıf veya teknoloji biçimini atamayız. Sonraki çağların dosyaları açılırken önceki çağla süreklilik ve kopuş bağları ayrıca araştırılır. Bu paketteki ilk bulgular bu yaklaşımın başlangıcıdır; bütün dünya tarih öncesinin tamamlandığı iddiası değildir.
