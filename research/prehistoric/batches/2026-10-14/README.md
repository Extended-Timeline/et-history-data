# 14 Ekim 2026 — native ihtiyaçlara bağlı veri toplama

Bu pakette **39 yeni kayıt ve 29 kaynak kaydı** bulunur. Üç bölgesel çalışma aynı
**GPT-6 Luna** ajanlarıyla yürütüldü; sağlık ve kurumsal süreçler için beş ek kayıt
ayrı hazırlandı. Kaynak kaydı sayısı, bütün yayınların ilk kez kullanıldığı veya
birbirinden bağımsız olduğu anlamına gelmez. Yeni bulgular site özetleri yerine
örneklem, evre, ölçüm ve değişim açıklamalarını ayrıntılandırır.

| Paket | Kayıt | Kaynak kaydı | Dosyalar |
|---|---:|---:|---|
| Batı Asya–Avrupa | 13 | 8 | [Veri](westasia-europe.yml), [kaynaklar](westasia-europe-sources.yml), [rapor](WestAsia-Europe.md) |
| Asya–Okyanusya | 10 | 8 | [Veri](asia-oceania.yml), [kaynaklar](asia-oceania-sources.yml), [rapor](Asia-Oceania.md) |
| Afrika–Amerikalar | 11 | 8 | [Veri](africa-americas.yml), [kaynaklar](africa-americas-sources.yml), [rapor](Africa-Americas.md) |
| Sağlık ve toplumsal süreçler | 5 | 5 | [Veri](processes.yml), [kaynaklar](processes-sources.yml), [rapor](Processes.md) |

Araştırmanın dayanağı [native tarihsel veri ihtiyaçları](../../../native-history-requirements/2026-10-13/README.md)
ve [durum/süreç kayıt sözleşmesidir](../../../native-history-requirements/2026-10-13/data-protocol.md).
Her bulgu ilgili gereksinim kimliklerine bağlıdır. Bir gereksinime bağlantı,
gereksinimin bütün bölgeler ve zaman aralıkları için tamamlandığı anlamına gelmez.

## Eklenen verinin niteliği

Bu pakette yerleşme alanı ve nüfus modelinin birbirinden ayrılması, üretim
alanlarının evrelerle izlenmesi, bitki kullanımının evcilleşmeden ayrılması,
beslenme ve hastalık örneklemlerinin sınırlarının korunması hedeflendi. Belirli
bir nesnenin tarihlendiği aralık ile topluluğun veya yerleşmenin bütün tarihi
birbirinin yerine kullanılmadı.

Veriler kaynakların kesinliğiyle saklanır. Bazı tarihler kalibre BCE, bazıları
kalibre BP, bazıları referans yılı belirtilmeyen göreli yaş veya arkeolojik
evredir. Sonraki çağlara uzanan yayın aralıkları korunur; bunların geç kısımları
tarih öncesi olayları gibi yorumlanmaz. Bu paketin bütün kayıtlarının MÖ 3000
öncesinde kaldığı iddia edilmez.

Yeni tarihlemenin eski kronolojiyle uyuşmadığı örneklerde kaynaklar ve
örneklemler ayrı tutuldu. Böyle bir bulgu, daha önceki bütün site kayıtlarını
tek işlemle değiştirmeyi haklı çıkarmaz. Aynı şekilde eski bir evcilleştirme
yorumuna itiraz eden yeniden inceleme, bitki varlığının bütün kanıtını ortadan
kaldırmış sayılmaz.

## Saklanan alanlar

- Tarihli bulgu ve gerçek coğrafi/örneklem kapsamı.
- Sayısal ölçüm varsa birim, payda veya modelin dayanağı.
- Gözlenen değişim veya dönem içi örüntü; kaynağın önerdiği mekanizma ve sınırları.
- Doğrudan kaynak, erişim düzeyi ve ilgili bölüm/tablo/şekil.
- Native araştırma maddeleriyle bağlantılar.
- `collected` durumu; belgelenmeyen oyun değerleri eklenmez.

## Kapsamın açık kalan tarafları

Bu çalışma tarih öncesinin tamamını kapsama hedefini ilerletir. Dünya çapında
eksiksiz nüfus, kimlik, dil, siyasi kontrol veya üretim haritası oluşturmaz.
Özellikle bağımsız kanıtla tanımlanmış siyasi ilişki tarafları ve yükümlülükleri,
ayrıntılı bölgesel dil kronolojileri, konum/yayılım geometrileri ve dönemler
arası bağlantılar hâlâ açık. Kaynakta tanımlanamayan hükümdar, din, devlet,
rota veya nüfus bileşimi uydurulmadı.

Önceki denetimde sayılan 98 kayda bu paket eklenince aynı seçilmiş koleksiyonun
ham toplamı **137** olur. Bu sayıya sınır bağlamları dahildir; yöntem notları,
tekrarlı eski dört-site paketi ve henüz kaynak denetiminden geçmemiş eski
repo varlıkları dahil değildir. 137, tamamlanmış ülke veya yerleşme sayısı değildir.

Dosya, kaynak, gereksinim ve tarih aralığı kontrolleri [validation.yml](validation.yml)
içinde; kaynaklı kanıtların native maddelerine bağlantıları
[coverage-update.yml](coverage-update.yml) içinde kayıtlıdır. Yapısal doğrulama
tarihsel kapsamın tamamlandığı veya her hipotezin kesinleştiği anlamına gelmez.
