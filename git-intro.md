# Git snabbintro

Skapa ett konto på [GitHub](https://github.com/).

## Installera Git

### Windows

Ladda ner och installera Git från [git-scm.com](https://git-scm.com/).

### macOS

Kommer förinstallerat på macOS.

## Skapa ett nytt repository

1. Gå till [GitHub](https://github.com/).
2. Klicka på "+" i övre högra hörnet och välj "New repository".
3. Fyll i namn och beskrivning.
4. Klicka på "Create repository".

## Skapa ett lokalt repository

Öppna terminalen och kör följande kommandon:

```bash
cd sökväg/till/ditt/projekt
git init
```

## Länka det lokala repositoryt med det på GitHub

```bash
git remote add origin "URL till ditt repository"
```

## Lägg till filer och gör en commit

```bash
git add . # Lägg till alla filer
git commit -m "Initial commit" # Gör en commit
```

## Pusha till GitHub

```bash
git push origin main
```

Du kommer säkerligen att stöta på ett problem här. Följ instruktionerna som visas i terminalen.

## Konfigurera Git

Öppna terminalen och kör följande kommandon:

```bash
git config --global user.name "Ditt namn" # Ditt namn eller användarnamn, spelar ingen roll
git config --global user.email "Din e-post" # Din e-post du använde för att skapa ditt GitHub-konto
```

## Skapa en .gitignore-fil

Skapa en fil som heter `.gitignore` i ditt projekt och lägg till filer och mappar som du inte vill ska pushas till GitHub.

T.ex:
```
.vscode/
```

## Lägg till en README.md

README fil kan vara bra att ha för att beskriva ditt projekt. Skriv en README.md fil i ditt projekt och skriv en beskrivning av ditt projekt.

## Koppla ihop ditt lokala repository med GitHub

```bash
git remote add origin "URL till ditt repository"
```

## Pusha till GitHub

```bash
git push origin main
```

## Bra att veta:


### Klona ett repository

```bash
git clone "URL till ditt repository"
```

### Hämta senaste ändringarna

```bash
git pull origin main
```

### Skapa en ny branch

```bash
git checkout -b "namn-på-branch"
```

### Byt branch

```bash
git checkout "namn-på-branch"
```

### Lägg till ändringar och gör en commit

```bash
git add .
git commit -m "Din commit"
```


### Pusha till GitHub

```bash
git push origin "namn-på-branch"
```

### Skapa en pull request

1. Gå till ditt repository på GitHub.
2. Klicka på "Pull requests".
3. Klicka på "New pull request".
4. Välj vilken branch du vill merga till main.
5. Klicka på "Create pull request".
6. Skriv en beskrivning av din pull request.
7. Klicka på "Create pull request".

### Merga en pull request

1. Gå till ditt repository på GitHub.
2. Klicka på "Pull requests".
3. Klicka på den pull request du vill merga.
4. Klicka på "Merge pull request".
5. Klicka på "Confirm merge".

### Ta bort en branch

```bash
git branch -d "namn-på-branch"
```

### Ta bort en remote branch

```bash
git push origin --delete "namn-på-branch"
```

### Se historik

```bash
git log
```

### Ångra senaste commit

```bash
git reset --soft HEAD~1
```

### Ångra senaste commit och ändringar

```bash
git reset --hard HEAD~1
```

### Ångra allt och gå tillbaka till en tidigare commit (OBS! Förlorar allt som inte är committat)
```bash
git reset --hard "commit-hash"
```

## Logga in på Github i terminalen
### Koppla din lokala git användare till GitHub

```bash
git config --global credential.helper cache
# eller
git config --global credential.helper store
```

Skillnaden mellan `cache` och `store` är att `cache` sparar dina uppgifter i 15 minuter medan `store` sparar dina uppgifter permanent.

### Spara din ssh-nyckel

Länk till anvisningar: [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```



