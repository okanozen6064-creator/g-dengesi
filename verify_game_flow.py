from playwright.sync_api import sync_playwright, expect

def run_verification(playwright):
    """
    Streamlit uygulamasının temel akışını doğrular:
    1. Parti seçimi yapar.
    2. Bir eylem gerçekleştirir.
    3. Sonucun ekran görüntüsünü alır.
    """
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        page.goto("http://localhost:8501", timeout=60000)

        expect(page.get_by_text("Partiler Savaşı'na Hoş Geldiniz!")).to_be_visible(timeout=30000)

        party_button = page.get_by_role("button", name="Ulusal Birlik Partisi (Sıkı Milliyetçilik)")
        expect(party_button).to_be_enabled(timeout=15000)
        party_button.click()

        # Ana oyun ekranının yüklenmesini bekle (Sidebar'daki Tur 1'i kontrol et)
        sidebar = page.locator("section[data-testid='stSidebar']")
        expect(sidebar.get_by_text("Tur: 1/48")).to_be_visible(timeout=15000)

        action_button = page.get_by_role("button", name="Geniş Kapsamlı Miting Düzenle")
        expect(action_button).to_be_enabled(timeout=15000)
        action_button.click()

        # **** YENİ SAĞLAM KONTROL ****
        # Arayüzün güncellenmesini ve Tur 2'ye geçilmesini bekle.
        # Bu, sayfanın yeniden yüklendiğini ve geri bildirim mesajının
        # artık DOM'da olduğunu garanti eder.
        expect(sidebar.get_by_text("Tur: 2/48")).to_be_visible(timeout=15000)

        # Artık geri bildirim mesajının görünür olduğunu güvenle doğrulayabiliriz.
        expect(page.get_by_text("'Geniş Kapsamlı Miting Düzenle' eylemi gerçekleştirildi.")).to_be_visible()

        screenshot_path = "/home/swebot/jules-scratch/verification/verification.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Ekran görüntüsü başarıyla alındı: {screenshot_path}")

    except Exception as e:
        print(f"Doğrulama sırasında bir hata oluştu: {e}")
        page.screenshot(path="/home/swebot/jules-scratch/verification/error_screenshot.png", full_page=True)

    finally:
        context.close()
        browser.close()

with sync_playwright() as playwright:
    run_verification(playwright)
