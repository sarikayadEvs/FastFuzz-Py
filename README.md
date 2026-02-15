🚀 FastFuzz-Py: Web Directory & File Discovery
Kendi siber güvenlik çalışmalarım için geliştirdiğim, Python tabanlı bir dizin ve dosya keşif aracı. Threading kullanarak tarama sürecini hızlandırıyor ve "Response Size" analizi yaparak gereksiz (false-positive) sonuçları temizliyor.

✨ Özellikler:
Çoklu İzlek (Multi-threading): Aynı anda birçok isteği paralel olarak gönderir.

Akıllı Filtreleme: Sunucunun her isteğe 200 OK döndürdüğü durumlarda, sayfa boyutuna bakarak gerçek sonuçları ayırır.

Uzantı Desteği: Sadece dizinleri değil, .php, .html, .txt gibi dosyaları da arar.

GUI Dosya Seçici: Wordlist dosyasını el ile yazmak yerine Windows penceresinden seçmenizi sağlar.

🛠️ Kullanım:
Projeyi indirin.

pip install requests komutuyla gerekli kütüphaneyi kurun.

python fuzzer.py komutuyla çalıştırın.

Hedef URL'yi girin ve wordlist dosyanızı seçin.
