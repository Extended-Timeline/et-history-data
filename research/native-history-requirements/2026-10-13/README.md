# Native sistemlerden türetilen tarihsel veri ihtiyaçları

**Tamamlanma durumu: veri toplama tamamlanmadı.** Son [kapsam denetimi](Completeness-Audit.md)
native örnekleri ile toplanmış kanıtları yeniden karşılaştırır. Aşağıdaki 76 madde
araştırma gereksinimidir; tamamlanmış veri paketleri değildir.

[14 Ekim toplama paketi](../../prehistoric/batches/2026-10-14/README.md) bu kataloğa
bağlı 39 yeni kayıt ekler. Aşağıdaki dokuz kayıt, 13 Ekim başlangıç paketinin
sayısıdır; sonraki koleksiyon ayrı izlenir.

Araştırmanın kapsamı, EU5'in kurulu native veri türlerinden çıkarıldı. Tarihsel içeriğin kaynağı bilimsel yayınlar ve tarihsel belgelerdir. Hedefimiz bir dönemin ülkelerini listelemekle sınırlı değildir: yerleşmelerin, toplumların, siyasi yapıların, üretimin ve ilişkilerin zaman içinde nasıl değiştiğini de kaynaklarıyla saklamaktır.

Üç **GPT-6 Luna** ajanının hazırladığı katalogda **76 araştırma maddesi** bulunuyor: toplum/kimlik için 24, siyaset için 25, maddi dünya için 27. Başlıkların bazıları birbirini tamamlar; bu sayı 76 bağımsız oyun sistemi anlamına gelmez. Native envanterinde 124 `in_game/common` klasörü ve 25 başlangıç dosyası kaydedildi. Grafik, UI ve AI ayarlarını tarihsel veri ihtiyacı olarak saymadık. Kurulum klasörünün adından oyun sürümü çıkarmadık.

## Native dosyalar bize hangi bilgileri araştırmamız gerektiğini söylüyor?

| Araştırılacak bilgi | Native karşılığı | Mevcut tarih öncesi araştırmasının açığı |
|---|---|---|
| Halklar, kültürler, diller ve adlar | `cultures`, `culture_groups`, `languages`, `language_families` | Arkeolojik kültür örnekleri var; bunların dil, öz kimlik ve sonraki topluluklarla bağlantıları ayrıca araştırılmalı. |
| İnanç, ritüel ve dini örgütlenme | `religions`, `religion_groups`, `religious_schools`, `holy_sites` | Anıt ve gömü örnekleri var; uygulamaların bölgesel yayılımı ve değişimi, yorum ayrılıkları eksik. |
| Nüfus, hareketlilik ve toplumsal roller | `define_pop`, `pop_types`, `estates` | Noktasal tahminler ve bazı hareketlilik bulguları var; bütün dönem için bölgesel nüfus dizileri ve rol dağılımları yok. |
| Siyasi oluşumlar ve toprak ilişkileri | Ülke başlangıç kayıtları, sahiplik/kontrol ayrımları, `country_ranks` | Erken merkez ve rekabet örnekleri var; siyasi bütünleşme, fiili etki alanı ve dağılma süreçleri yeterince belgelenmedi. |
| Kişiler, soy ilişkileri ve iktidar devri | `characters`, `dynasties`, `heir_selections`, `ruler_term` | Akrabalık örnekleri adlandırılmış hükümdar veya hanedan sağlamaz. Bilinebilir erken kişiler ayrıca doğrulanmalı; diğer alanlar bilinmeyen kalmalı. |
| Yönetim, hukuk ve otorite | `government_types`, `government_reforms`, `laws`, `estate_privileges`, `societal_values` | İdare ve statüye ilişkin buluntular var; otoritenin nasıl örgütlendiği ve değiştiği için ayrı kanıt gerekiyor. |
| Diplomasi, bağımlılık ve ortak örgütler | Diplomasi başlangıcı, `subject_types`, `international_organizations` | İncelenen koleksiyonda tarafları ve yükümlülükleri belirleyen hedefli bir tarih öncesi veri paketi bulunmadı. Ticaret ilişkisi bunların yerine geçmez. |
| Çatışma, askeri örgütlenme ve araçlar | Savaş başlangıcı, `unit_types`, `levies`, `wargoals` | Şiddet ve yıkım örnekleri var; aktörler, örgütlenme, araçların değişimi ve alternatif açıklamalar genişletilmeli. |
| Yerleşme hiyerarşisi ve kentleşme | `location_ranks`, `town_setups`, `building_types` | Site listeleri var; her evrede alan, işlev, yoğunluk, ağ içindeki konum, büyüme ve terk edilme dizileri eksik. |
| Tarım, hayvancılık ve beslenme | `goods`, `production_methods`, pop gıda alanları | Bölgesel başlangıç örnekleri var; benimseme, karma geçim biçimleri ve üretim değişimleri izlenmeli. |
| Kaynak çıkarımı ve zanaat üretimi | `goods`, `production_methods`, üretim binaları | Buluntu ile yerel üretim ayrımını kuracak maden/ocak, üretim artığı, ölçek ve evre verileri gerekiyor. |
| Değişim ağları ve ulaşım | Pazar başlangıcı, `road_types`, yol ağları | Malzeme kökeni örnekleri var; güzergâh, aracılar, ağ değişimi ve miktar çoğunlukla açık. |
| Teknoloji, bilgi ve kurumsal yayılım | `advances`, `institution`, kurum başlangıcı | İlk buluntu örnekleri var; yerel benimseme, kullanım farkları, terk ve aktarım mekanizmaları araştırılmalı. |
| İklim, su ve tarihsel peyzaj | `climates`, `vegetation`, `topography` | Geniş çevre örnekleri var; yerleşme evreleriyle eşleşen yerel kıyı, nehir ve habitat dizileri eksik. |
| Hastalık ve sağlık | `diseases`, salgın başlangıcı | Önceki incelenen koleksiyonda hedefli kayıt bulunmadı. Yeni tekil patojen bulgusu bir başlangıç; salgın ve demografik etki ayrı sorular. |
| Sanat, anıt ve bilgi aktarımı | `artist_work`, sanat başlangıcı | Nesne ve anıt örnekleri var; üretim bağlamı, kullanım değişimi, dolaşım ve yorum sınırları genişletilmeli. |

Tablodaki “eksik”, araştırılan koleksiyonda kapsamanın yetersiz olduğu anlamına gelir. Bir olgunun tarihte bulunmadığı anlamına gelmez. Önceki bulguların ID'leri ve denetlenen kapsam [coverage.yml](coverage.yml) içinde; yeni dokuz bulgu ayrı dosyalardadır.

## Durum kadar değişimi de toplamak

Her kategori için **nerede/ne zaman/ne vardı** sorusunun yanında **ne değişti/hangi kanıtla/hangi açıklamalarla** soruları var. Örneğin:

- Yerleşmeler için kuruluş, büyüme, işlev değişimi, yeniden yerleşme ve terk.
- Siyasi yapılar için oluşum, bütünleşme, bölünme, fetih ve yönetim değişimi.
- Ekonomi için üretim tekniğinin benimsenmesi, uzmanlaşma, kaynak ve değişim ağlarının dönüşümü.
- Dil, kültür ve inanç için süreklilik, temas, benimseme, ayrışma ve birleşme; nüfus ile yönetici grubun ayrı seyirleri.
- Çevre ve sağlık için değişimin kendisi ile insanların buna verdiği tepkinin ayrı kanıtları.

Takvimde çağ değişmesi, bütün toplumların aynı dönüşümü yaşadığı anlamına gelmez. Bir süreç iki veya daha fazla araştırma sınıfını aşabilir. Sonraki çağlara geçildiğinde bağlantı, yalnızca benzer isimler veya sonradan çizilmiş soy ağacıyla kurulmayacak; her süreklilik ve kopuş iddiası kaynaklandırılacak.

Native `ethnicities` dosyalarındaki gen ve görünüş seçenekleri bir tarihsel halk kataloğu sağlamıyor. Halk, dil, kültür, siyasi aidiyet, arkeolojik etiket ve biyolojik soy ayrı izlenecek. Kullanıcının halkların dönüşümü örneği bu geniş araştırmanın bir bileşenidir.

## İlk yeni toplama paketi

Yeni dosyalarda **9 kaynaklı bulgu ve 11 kaynak kaydı** bulunuyor. Bunlar geniş kapsamın başlangıcıdır:

- [Toplum ve kimlik](societies-research.yml): erken çiftçi topluluklarında yerel soy sürekliliği, bölgeden bölgeye değişen çiftçi–avcı-toplayıcı etkileşimi ve Karadeniz/step temasının yorumları.
- [Siyasi ve toplumsal örgütlenme](politics-research.yml): Hongshan tören merkezlerinin farklılaşması, hane rollerinin incelenmesi ve üretim/erişim ilişkileri. Üçü aynı bölgeyi derinleştirir; dünya çapında siyasi tarih kapsaması oluşturmaz.
- [Maddi dünya](material-world-research.yml): kıyı yerleşmesinin çevresel uyumu ve terk edilmesi, tarih öncesi patojen tespiti, kaya sanatının tarihleme kanıtı.

Her kaydın mekanizma ve genelleme sınırları bulunuyor. Bazıları değişim dizisi, bazıları dönem içi gözlem sunar. Tekil bir enfeksiyondan salgın; haneler arası farktan hanedan; genetik karışımdan dil veya etnik kimlik üretmedik. Kaynak özetiyle sınırlı okunabilen yayınlar açıkça işaretlendi. Bu bulguların doğrulandığı ayrıntı düzeyi, doğrudan oyun için eksiksiz veri olduğu anlamına gelmez.

## Dosyalar ve devam eden araştırmanın ölçütü

| Dosya | İçerik |
|---|---|
| [societies.md](societies.md), [societies.yml](societies.yml) | Toplum, kimlik, dil, inanç ve demografi; native anahtarlar ve tarihsel sorular |
| [politics.md](politics.md), [politics.yml](politics.yml) | Siyasi yapı, hukuk, kişiler, ilişkiler ve çatışma |
| [material-world.md](material-world.md), [material-world.yml](material-world.yml) | Yerleşme, üretim, ulaşım, teknoloji, çevre, sağlık ve sanat |
| `*-research.yml`, `*-sources.yml` | Yeni bulgular, kaynakları, tarihleme ve yorum sınırları |
| [data-protocol.md](data-protocol.md) | Durum ve süreç kayıtları; kanıt, yorum ve oyun kuralı ayrımı |
| [coverage.yml](coverage.yml) | Önceki tarih öncesi araştırmasının somut dayanakları ve açık soruları |
| [native-inventory.yml](native-inventory.yml) | Native kategori ve başlangıç dosyası envanteri |
| [scope.yml](scope.yml) | Dönem kapsamı ve tarihsel olmayan ayarların ayrılması |
| [validation.yml](validation.yml) | Yapısal kontrolün kapsamı ve sonucu |

İlk ayrıntılı hedef **tarih öncesi çağının tamamı** olarak korunuyor. Bölgesel paketler bu 16 başlığın ilgili olanlarını tarih aralıklarıyla değerlendirmeli. Bir alan uygulanamıyorsa gerekçesi, bilinmiyorsa kanıt sınırı, tartışmalıysa alternatifleri yazılmalı. Önceki [teknik karşılaştırma](../../native-comparison/2026-10-13/README.md) dönüştürme ve uygulama sorunlarının ayrı arşividir; tarih araştırmasının kapsamını belirlemez.
