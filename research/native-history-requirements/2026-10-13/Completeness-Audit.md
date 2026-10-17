# Veri toplama tamamlanmış mı?

**Hayır. Native sistemlerin gerektirdiği tarihsel kapsamı dolduracak bütün veriler toplanmadı.** Bu denetim, özellikle aktif hedef olan tarih öncesinin tamamı için yapılmıştır. Diğer çağların tam kapsandığına ilişkin bir onay da verilmemiştir.

Önceki 76 maddelik katalog araştırılacak soruları tanımlar. 76 tamamlanmış veri paketi anlamına gelmez. Önceki `validation.yml` dosyasındaki `passed`, belirtilen yapısal kontrollerin geçtiği anlamına gelir; veri toplamanın tamamlandığını göstermez.

## Yeniden kontrol edilenler

- Native `in_game/common` altında 124 klasör; `main_menu/setup/start` altında 25 dosya tekrar sayıldı. 25 başlangıç dosyasının SHA-256 değerleri önceki native envanteriyle aynı.
- Geniş tarih öncesi koleksiyonundaki 77, önceki alan odaklı paketteki 12 ve son paketteki 9 kayıt doğrudan yeniden sayıldı: **98 ayrı bulgu**. Dönem sınırını aşan ve sonraki döneme bağlam sağlayan kayıtlar bu ham sayıya dahildir. Önceki dört tekrarlı site kaydı ve yöntem notları bu sayıya dahil değildir.
- Son dokuz bulgu, 76 gereksinimin 20 farklı maddesine açık bağlantı taşıyor. Bir bağlantı, o gereksinimin tamamlandığı anlamına gelmez. Önceki bulguların ilgili başlıkları desteklemesi mümkündür; kalan 56 maddeyi “hiç veri yok” diye sınıflandırmadık.
- Önceki kapsam dosyasındaki 16 başlık yeni bulgularla birlikte tekrar değerlendirildi. **Hiçbir başlık için dünya çapındaki dönem kapsamının tamamlandığı gösterilemiyor.** Hastalık başlığı artık tekil bir patojen gözlemi içeriyor. Diplomasi/bağımlılık için incelenen koleksiyonda taraf ve yükümlülükleri belgeleyen hedefli bir paket bulunamadı.

Bu denetimin birimi tarihsel kaynaklı araştırma koleksiyonudur. Repodaki bütün eski ülke ve karakter kayıtlarının kaynak doğrulaması tamamlanmış kabul edilmez. Bulgu sayısından bir tamamlanma yüzdesi hesaplanmaz.

## Native örnekler ile somut açıklar

| Native dosya ve alan | Toplanmış kanıtın düzeyi | Eksik veri |
|---|---|---|
| `06_pops.txt:3–10`: `define_pop`, `type`, `size`, `culture`, `religion` | Bir yerleşme için nüfus modeli ve seçilmiş demografik/soy bulguları | Bölgesel nüfus dizileri, birim ve belirsizlik, nüfusun bileşimi ve değişimi; bilinmeyen kültür/din/rol alanları açık tutulmalı. |
| `cultures/00_cultures.info:2,22–26`: dil ve kültür grupları | Arkeolojik etiketler ve bazı soy sürekliliği/temas çalışmaları | Dillerin ve tarihsel kimliklerin coğrafi-zamansal dağılımı; adlandırma ve değişim ilişkilerinin bağımsız kanıtı. |
| `07_cities_and_buildings.txt:4–5`: `rank`, `town_setup` | Seçilmiş site ve anıt evreleri | Yerleşme alanı, işlev, bölgesel hiyerarşi, kuruluş/büyüme/terk sırası; çağdaş peyzaj ve konum. |
| `goods/00_raw_materials.txt:2–14`: üretim yöntemi ve mal kategorileri | Evcilleştirme, malzeme ve bazı üretim örnekleri | Bölge ve evre bazında üretim yerleri, yoğunluğu, teknikleri, ithalat/yerel üretim ayrımı, değişim mekanizmaları. Native fiyatlar tarihsel fiyat sayılmaz. |
| `03_markets.txt:1–5`, `09_roads.txt:2–10`: pazar merkezleri ve bağlantılar | Bazı malzeme kökeni/temas bulguları | Kaynak–hedef ağları, güzergâh kanıtı, ulaşım ve ağların zaman içindeki değişimi. Bir malın kökeni tek başına yol veya pazar kanıtı değildir. |
| `08_institutions.txt:3–9`: yerleşme bazında kurum varlığı | İdare, yazı ve uzmanlaşmaya ilişkin seçilmiş örnekler | Bir uygulamanın hangi bölgede, hangi tarihte benimsendiği, ne kadar yayıldığı ve nasıl değiştiği. Orta Çağ kurumu tarih öncesine aynen atanmaz. |
| `10_countries.txt:15–80`: siyasi aktör, kontrol, yönetim, hükümdarlık | Bazı erken merkez, rekabet ve sosyal farklılaşma bulguları | Siyasi oluşum ve bütünleşmenin kronolojisi, fiili etki alanı, otorite biçimi; tanımlanabilir kişiler/iktidar devri için ayrı kanıt. |
| `12_diplomacy.txt:6–16`: taraflar, bağımlılık türü ve tarih | Hedefli tarih öncesi ilişki paketi bulunmadı | Kanıt varsa taraflar, yükümlülük, yön, zaman ve değişim; benzer eserlerden ittifak veya haraç ilişkisi çıkarılmaz. |
| `16_wars.txt`, `27_armies.txt:2–11`: çatışma tarafları, birimler ve komuta | Şiddet/yıkım ve araç örnekleri | Bölgesel çatışma dizileri, aktörler, örgütlenme ve askeri araçların değişimi. Buluntu sayısı asker sayısı değildir; bilinmeyen taraf ve liderler doldurulmaz. |
| `climates`, `vegetation`, `topography` | Bazı çevre dizileri ve tekil kıyı uyumu örneği | Yerel kıyı, nehir, iklim ve habitat evreleri; yerleşme/üretim değişimlerine bağlanan tarih ve nedensellik kanıtı. |
| `19_diseases.txt:1–20`: hastalık, köken ve yayılım alanları | Tek bireyde patojen tespiti | Yaygınlık, salgın, aktarım ve nüfus etkisi; bunlar tek örnekten çıkarılamaz. Buradaki salgın açıklamaları yorum satırlarındaki native şema örnekleridir. |
| `11_art.txt:1–7`: nesne, yer, köken ve tarih | Seçilmiş sanat/nesne örnekleri | Bölgesel üretim ve kullanım bağlamları, dolaşım, işlev ve değişim; anlam yorumlarının sınırları. Kalite puanı tarihsel ölçüm değildir. |

## Önceki katalogda ayrıca ayrıntılandırılması gereken alt sistemler

Native dosyaların yeniden taranması, geniş başlıkların altında daha açık araştırma sorularına ihtiyaç olduğunu da gösterdi:

| Native kanıt | Ek araştırma sorusu | Uygulanabilirlik |
|---|---|---|
| `bureaucracies/byz.txt:1–23` | İdari görevlerin, görevlilerin ve yetki dağılımının ortaya çıkması/değişmesi | Native Bizans örneği tarih öncesine taşınmaz; yalnızca desteklenen yerel idare biçimleri araştırılır. |
| `parliament_types/00_default.txt:1–30` | Karar alma toplantıları, konseyler ve katılım biçimleri | Arkeolojik topluluk otomatik olarak parlamento veya meclis sayılmaz. |
| `regencies/00_fratricide_succesion.txt:2–16` | Vekâlet, iktidar boşluğu ve geçiş dönemleri | Tanımlanabilir kurum ve kişiler için kanıt varsa; bilinmeyen tarih öncesi hükümdarlar üretilmez. |
| `religious_figures/00_muslim.txt:1–5` | Dini uzmanlık, görev ve otorite | Native din/ünvan aynen atanmaz; kanıtlanan yerel roller ayrı araştırılır. |
| `gods/common.txt:1–13` | Adlandırılmış ilahlar ve dini anlatıların zaman/coğrafya kapsamı | Yazılı veya başka bağımsız kanıt gerekiyorsa; figürinden ilah adı türetilmez. |
| `employment_systems/00_default.txt:1–29` | Emek tahsisi, üretime katılım ve yükümlülükler | Oyun öncelik puanları tarihsel gerçek değildir; kaynaklı toplumsal ilişkiler araştırılır. |
| `23_colonies.txt:1–16` | Örgütlü yerleşim genişlemesi, aktörler ve hak iddiaları | Göç veya yeni yerleşme doğrudan devlet destekli koloni anlamına gelmez. |
| `24_town_rights.txt:1–5`, `town_rights/11_scandinavian.txt:6–23` | Yerleşmeye bağlı haklar, yükümlülükler ve bunların değişimi | Kanıtlanabilir yerel kurumlarda; Orta Çağ kent hakkı tarih öncesine atanmaz. |

Bunlar sekiz yeni tarihsel veri paketi toplanmış demek değildir. Ayrıntılandırılması gereken alt sorulardır. Native sisteme karşılık bulunması, o sistemin her dönemde tarihsel karşılığı olduğu anlamına gelmez.

## Tamamlandı diyebilmek için

Her araştırılan bölge ve evre için ilgili başlıkların kaynaklı durumları, önemli değişimleri ve açıklamalarının kanıtı bulunmalı; kapsam dışı, bilinmeyen ve tartışmalı alanlar ayrıca kaydedilmeli. Yerleşme veya malzeme örneği bütün bölgeyi temsil etmemeli. Dönemler arası süreklilik ve kopuş iddiaları kaynaklandırılmalı.

Şu an bu koşullar sağlanmıyor. Hazır olanlar veri ihtiyacı kataloğu, yöntem ve başlangıç kanıt koleksiyonudur. Kaynak toplama ve bölgesel süreç araştırması devam gerektiriyor. Kanıtın bilinmediği tarih öncesi alanların tamamını sayısal değer veya adlarla doldurmak bir tamamlanma ölçütü olamaz.

Makineyle denetlenebilen sayımlar ve bu sonucun sınırları [completeness-audit.yml](completeness-audit.yml) içinde tutulur.
