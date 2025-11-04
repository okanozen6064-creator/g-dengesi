from playwright.sync_api import sync_playwright, expect
import re

def run_verification(playwright):
    """
    "İktidar Döngüsü" mekaniklerini doğrular. Expander için bekleme eklendi.
    """
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        print("1. Uygulamaya gidiliyor...")
        page.goto("http://localhost:8501", timeout=60000)

        print("2. Parti seçim ekranı bekleniyor...")
        expect(page.get_by_text("Bir Lider Seç, Bir Ülke Yönet")).to_be_visible(timeout=30000)

        print("3. Parti expander'ı açılıyor...")
        page.get_by_text(re.compile(r"Ulusal Birlik Partisi.*")).click()

        # Expander'ın açılması ve içeriğinin render olması için kısa bir bekleme ekle
        page.wait_for_timeout(500)

        print("4. Parti seçim butonu bekleniyor ve tıklanıyor...")
        party_button = page.get_by_role("button", name="'Ulusal Birlik Partisi' ile Başla")
        expect(party_button).to_be_enabled(timeout=15000)
        party_button.click()

        print("5. Oyunun başlaması (Yıl: 1) bekleniyor...")
        sidebar = page.locator("section[data-testid='stSidebar']")
        expect(sidebar.get_by_text("Yıl: 1")).to_be_visible(timeout=15000)
        expect(sidebar.get_by_text("Eylem Puanı (EP)5 / 5")).to_be_visible()

        print("6. Bir eylem gerçekleştiriliyor...")
        action_button = page.get_by_role("button", name="Propaganda Kampanyası Başlat")
        expect(action_button).to_be_enabled()
        action_button.click()

        print("7. EP'nin azalması (EP: 4) bekleniyor...")
        expect(sidebar.get_by_text("Eylem Puanı (EP)4 / 5")).to_be_visible(timeout=15000)

        print("8. 'Yılı Bitir' butonuna tıklanıyor...")
        end_year_button = page.get_by_role("button", name="Yılı Bitir")
        expect(end_year_button).to_be_enabled()
        end_year_button.click()

        print("9. Yeni yıla geçilmesi (Yıl: 2) ve EP'nin yenilenmesi bekleniyor...")
        expect(sidebar.get_by_text("Yıl: 2")).to_be_visible(timeout=15000)
        expect(sidebar.get_by_text("Eylem Puanı (EP)5 / 5")).to_be_visible()

        print("10. Ekran görüntüsü alınıyor...")
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
