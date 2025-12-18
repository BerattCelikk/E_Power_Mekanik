from django.shortcuts import render, redirect
from products.models import Product
from .models import ContactMessage

def home(request):
    products = Product.objects.all().order_by('-created_at')[:3]
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def career(request):
    return render(request, 'career.html')

def kvkk(request):
    return render(request, 'kvkk.html')

def terms(request):
    return render(request,'terms.html')

def gearbox_detail(request):
    return render(request, 'gearbox_detail.html')

def differential_detail(request):
    return render(request, 'differential_detail.html')

def services(request):
    return render(request,'services.html')

def privacy(request):
    return render(request,'privacy.html')

def products(request):
    return render(request,'products.html')
def news(request):
    # Tüm haberlerin listesi (Veritabanı yerine sözlük listesi)
    all_posts = [
        {
            'slug': 'futurelab-roportaji',
            'title': 'E-Power Mekanik Futurelab Röportajı',
            'date': '15 Ara, 2023',
            'author': 'Admin',
            'category': 'Etkinlikler',
            'image_url': 'images/slider1.jpeg',
            'excerpt': 'Futurelab etkinliğinde gerçekleştirdiğimiz röportajda, yerli şanzıman teknolojilerimiz ve gelecek vizyonumuz hakkında konuştuk.'
        },
        {
            'slug': 'yeni-arge-merkezi',
            'title': 'Yeni AR-GE Merkezimiz Açıldı',
            'date': '20 Kas, 2023',
            'author': 'Admin',
            'category': 'Kurumsal',
            'image_url': 'images/slider2.png',
            'excerpt': 'Teknolojik altyapımızı güçlendirmek amacıyla kurduğumuz yeni AR-GE merkezimiz faaliyete geçti.'
        }
    ]

    # 1. Arama Filtresi (q parametresi)
    query = request.GET.get('q')
    if query:
        all_posts = [post for post in all_posts if query.lower() in post['title'].lower()]

    # 2. Kategori Filtresi (category parametresi)
    category_filter = request.GET.get('category')
    if category_filter:
        all_posts = [post for post in all_posts if post['category'] == category_filter]

    # Kategori sayılarını hesapla (Sidebar için)
    category_counts = {
        'Tüm Haberler': len([p for p in all_posts if not category_filter]), # Toplam sayı (filtresiz)
        'Etkinlikler': len([p for p in all_posts if p['category'] == 'Etkinlikler']),
        'Kurumsal': len([p for p in all_posts if p['category'] == 'Kurumsal'])
    }
    
    # Eğer kategori seçiliyse, o kategorideki sayı o anki liste uzunluğudur
    if not category_filter:
         category_counts = {
            'Tüm Haberler': 2, # Toplam sabit sayı
            'Etkinlikler': 1,
            'Kurumsal': 1
        }

    context = {
        'posts': all_posts,
        'category_counts': category_counts
    }

    return render(request, 'news.html', context)
def news_detail(request, slug):
    # Veritabanı yerine geçici olarak bir sözlük (dictionary) kullanıyoruz.
    # Her haberin 'slug'ı (linki) anahtar kelime olarak belirlendi.
    
    news_data = {
        # 1. HABER: Futurelab Röportajı
        'futurelab-roportaji': {
            'title': 'E-Power Mekanik Futurelab Röportajı',
            'date': '15 Ara, 2023',
            'author': 'Admin',
            'category': 'Etkinlikler',
            'image_url': 'images/slider1.jpeg', 
            'body': """
                <p class="lead">Futurelab etkinliğinde gerçekleştirdiğimiz röportajda, yerli şanzıman teknolojilerimiz ve gelecek vizyonumuz hakkında konuştuk.</p>
                <p>E-Power Mekanik olarak katıldığımız bu prestijli etkinlikte, elektrikli araç sektörünün geleceğini şekillendiren teknolojileri masaya yatırdık. Sektör paydaşlarıyla bir araya gelerek, Türkiye'nin yerli ve milli üretim gücünün artırılması konusundaki kararlılığımızı vurguladık.</p>
                <br>
                <h3>Yerli Üretimin Önemi</h3>
                <p>Röportaj sırasında Genel Müdürümüz, özellikle dışa bağımlılığı azaltacak yerli mühendislik çözümlerinin önemine dikkat çekti. Kendi AR-GE merkezimizde geliştirdiğimiz diferansiyel ve dişli kutusu sistemlerinin teknik detayları katılımcılar tarafından büyük ilgi gördü.</p>
                <blockquote>"Geleceğin gücünü tasarlarken, yerli kaynakları en verimli şekilde kullanmayı ve global pazarda rekabetçi ürünler ortaya koymayı hedefliyoruz."</blockquote>
                <p>Fuarda sergilenen prototip ürünlerimiz, yüksek verimlilik değerleri ve sessiz çalışma prensipleriyle ziyaretçilerden tam not aldı. Gelecek projelerimizde bu teknolojileri daha da ileriye taşıyarak, elektrikli mobilite ekosistemine katkı sağlamaya devam edeceğiz.</p>
            """
        },

        # 2. HABER: Yeni AR-GE Merkezi
        'yeni-arge-merkezi': {
            'title': 'Yeni AR-GE Merkezimiz Açıldı',
            'date': '20 Kas, 2023',
            'author': 'Admin',
            'category': 'Kurumsal',
            'image_url': 'images/slider2.png',
            'body': """
                <p class="lead">Teknolojik altyapımızı güçlendirmek amacıyla kurduğumuz yeni AR-GE merkezimiz, modern laboratuvarları ve test sahalarıyla faaliyete geçti.</p>
                <p>Yenilikçi projelerimize hız kazandırmak ve mühendislik kabiliyetlerimizi bir üst seviyeye taşımak için tasarlanan yeni merkezimiz, son teknoloji simülasyon ve test cihazlarıyla donatıldı. Bu yatırım, E-Power Mekanik'in sektördeki öncü konumunu pekiştirecek stratejik bir adımdır.</p>
                <br>
                <h3>Merkezde Neler Var?</h3>
                <ul>
                    <li><strong>Gelişmiş Test Laboratuvarları:</strong> Dişli dayanıklılık ve ömür testleri için özel üniteler.</li>
                    <li><strong>Prototip Atölyesi:</strong> Tasarımların hızlı bir şekilde fiziksel parçalara dönüştürülmesini sağlayan CNC ve 3D yazıcı parkuru.</li>
                    <li><strong>Simülasyon Odaları:</strong> Akışkanlar dinamiği ve yapısal analizlerin yapıldığı yüksek performanslı bilgisayar sistemleri.</li>
                </ul>
                <p>Yeni merkezimizle birlikte, proje geliştirme süreçlerimizi %40 oranında hızlandırmayı ve müşteri taleplerine çok daha hızlı yanıt vermeyi hedefliyoruz. Bu merkez, sadece bir çalışma alanı değil, aynı zamanda mühendislerimiz için bir inovasyon üssü olacaktır.</p>
            """
        }
    }

    # URL'den gelen slug'a göre doğru haberi çekiyoruz
    post = news_data.get(slug)

    # Eğer haber bulunduysa detay sayfasına gönder, yoksa haberler sayfasına geri dön
    if post:
        return render(request, 'news_detail.html', {'post': post})
    else:
        # Opsiyonel: 404 sayfası yerine haberler ana sayfasına yönlendiriyoruz
        return redirect('news')

def contact(request):
    context = {}
    
    if request.method == 'POST':
        # Formdan verileri al
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '-')   # Telefon (Opsiyonel)
        subject = request.POST.get('subject', '-') # Konu (Opsiyonel)
        raw_message = request.POST.get('message') # Asıl mesaj
        
        # Telefon ve Konuyu mesaja ekle (Çünkü veritabanında ayrı sütun açmadık, pratik çözüm)
        full_message = f"Telefon: {phone}\nKonu: {subject}\n\nMesaj:\n{raw_message}"
        
        # Veritabanına kaydet
        if name and email and raw_message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=full_message
            )
            # Başarı mesajını sayfaya gönder
            context['success_message'] = "Mesajınız başarıyla gönderildi! En kısa sürede dönüş yapacağız."
            
    return render(request, 'contact.html', context)