# Teorifrågor

1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
Svar:Enhetstest testar en liten del av koden, exempelvis en funktion. 
Integrationstest: testar så flera delar fungerar med varandra. Regressionstest kontrollerar att tidigare funktionalitet inte gått sönder efter en ändring i kod. 
Prestandatest: Används vid testning av hastighet och belastning av vad systemet klarar av. 


2. Beskriv hur det går till när man arbetar med TDD.
Svar: Test-driven development, innebär att man skriver tester innan man börjar med programkoden. 
Man börjar med att skriva ett test för funktion som inte finns än, och testet misslyckas. 
Sen börjar man koda tills testet blir godkänt.
Sist när testet fungerar så börjar man förbättra kod utan ändring av funktionalitet, och tester körs igen för att säkra att allting fungerar. 
Och så går denna loop runt under hela processen.


3. Beskriv hur BDD skiljer sig från TDD.
Svar: BDD fokuserar sig mer på användarens beteende och krav, medans TDD fokuserar på kod och funktioner. 


4. Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend.
Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.
Svar: Jag tror att alla tester skulle användas av den anledning att de har olika användningsområden. 
Enhetstest för att testa mindre delar, funktioner och metoder i backend då det kan hitta fel tidigt i processen. 
Integrationstest för att kontrollera att olika delar av systemet funkar tillsammans. 
Sedan är det bra med e2e tester och testa användarflöden, exempel att användare kan facoritmarkera en bok. 
Och viktigt att ha med regressiontester för att säkra att tidigare funktionalitet fortfarande funkar när ny kod läggs in. 