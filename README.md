# Läslistan - Examination

## Vad som testas
### Backend:
- Funktion för att lägga till böcker i bookstore
- Funktion för att markera och avmarkera favoriter
- Funktion för att hantera fler böcker i katalogen
- Funktion för att lägga till och ta bort böcker i favoritebooks
- Integrationstest som kontrollerar samspoel mellan bookstore och favoritebooks


### Frontend:
- Att bokkatalogen visas korrekt i webbläsaren
- Användaren kan lägga till en ny bok via UI
- Användare kan markera och ta bort favoriter
- Statistik sidan går att öppna och visar innehåll
- Navigera mellan sidor

### Teststrategi
- Enhetstester (pytest) 
- integrationstester används för testa samspel mellan bookstore och favoritebooks
- BDD och e2e tester, (behave och playwright) används för användareflöden i webbläsare


# Starta projekt

## Installera 
py -m pip install -r requirements.txt :

- pytest
- behave
- playwright
- pytest-playwright


- playwright install

## Köra tester

### Backend tester
py -m pytest

### e2e tester
py -m behave tests/e2e/features



Arbetat med G-kraven och några VG krav