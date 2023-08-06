# package_model

Istruzioni per creare un modulo Python e condividerlo con *pip install [package_model]*.

(fonte utilizzata: https://www.youtube.com/watch?v=FkmtmYFTlYE)

# 1) Creazione di un pacchetto python e installazione locale 

Creare la seguente struttura ad albero:

```
package_model/
├── LICENSE
├── package_model
│   ├── example.py
│   └── __init__.py
├── README.md
└── setup.py
```

Il file *setup.py* sarà il file che Pip andrà a leggere quando eseguiremo l'istallazione del pacchetto e contiene le seguenti istruzioni:

```
from setuptools import setup

setup(name='package_model',
      version=0.1,
      description='Compute the square of a number',
      author='Lorenzo Marini',
      packages=['package_model'],
      zip_safe=False)

```

Passiamo adesso al file *__init__.py*. Al suo interno scriviamo:

```
from .example import quadrato
```

In questo modo, saremo ingrado di importale le singole funzioni (in questo caso solo una: 'quadrato') del nostro modulo *exmaple.py*

Adesso, siamo pronti per installare il nostro pacchetto localmente sul nostro computer.
Per fare ciò, dobbiamo semplicemente lanciare il seguente comando:

```
pip install .
```

NB: da lanciare dalla cartella principale del pacchetto (in cui è presente il file *setup.py*).

Vediamo l'output:
```
lorenzomarini@lorenzomarini-MacBookPro:~/Desktop/package_model$ pip install .
Defaulting to user installation because normal site-packages is not writeable
Processing /home/lorenzomarini/Desktop/package_model
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: package-model
  Building wheel for package-model (setup.py) ... done
  Created wheel for package-model: filename=package_model-0.1-py3-none-any.whl size=13830 sha256=c136a22a940ad2fb620893b33d8773964c62772ca34fbe40bdbf5bc3b2c47548
  Stored in directory: /tmp/pip-ephem-wheel-cache-p3gp0w1j/wheels/d6/1a/c0/6e22efdbc48c105b11d87f65f2062245a1a801b8b91f0c5711
Successfully built package-model
Installing collected packages: package-model
Successfully installed package-model-0.1
```
Abbiamo installato il nostro package sul nostro computer!

Per essere sicuri che tale pacchetto sia installato e salvato tra i vari pacchetti, diamo il comnado:

```
pip list
```
e verifica che *package_model* sia all'interno della lista.

# 2) Caricamento del pacchetto sul repositorio PyPi

Ora comincia la parte più eccitante...
Siamo pronti per caricare il nostro package nel repositorio di **PyPi**

NB: ci sono 2 repositori di nostro interesse.

Essi sono:
- **PyPi** per il testing (https://test.pypi.org/manage/projects/)
- il repositorio **PyPi** regolare (https://pypi.org/manage/projects/)

Attenzione: i due repositorio non sono la stessa cosa. Ciascuno ha il proprio account

Per caricare il pacchetto, dobbiamo prima altri file: **licence.txt**, **setup.cfg** e **README.md**.

Questi tre file addizionali sono necessari per poter caricare il nostro pacchetto su PyPi.

Il file fondamentale è **setup.cfg** e al suo interno vanno scritti i metadati che il pacchetto sta utilizzando.

```
[metadata]
description-file = README.md
```

Adesso, scriviamo qualcosa dentro **licence.txt**. Potremmo copiare semplicemente quanto scritto nella licenza generata automaticamente da GitHub al momento della creazione del repositorio.

Finalmente, siamo pronti per caricare il nostro pacchetto nel repositorio di PyPi.

Dobbaimo prima creare un *single model TAR file*. Per fare ciò, utilizziamo il file **setup.py** con il comando sdist.
La struttura ad albero che abbiamo ottenuto è la seguente:

```
package_model/
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── package_model
│           ├── example.py
│           └── __init__.py
├── LICENSE
├── package_model
│   ├── example.py
│   ├── __init__.py
│   ├── licence.txt
│   ├── README.md
│   └── setup.cfg
├── package_model.egg-info
│   ├── dependency_links.txt
│   ├── not-zip-safe
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── README.md
└── setup.py
```

Quindi, digitiamo il seguente comando per creare il file TAR:

```
python3 setup.py sdist
```

Vediamo la nuova struttura ad albero:

```
package_model/
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── package_model
│           ├── example.py
│           └── __init__.py
├── dist
│   └── package_model-0.1.tar.gz
├── LICENSE
├── package_model
│   ├── example.py
│   ├── __init__.py
│   ├── licence.txt
│   ├── README.md
│   └── setup.cfg
├── package_model.egg-info
│   ├── dependency_links.txt
│   ├── not-zip-safe
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── README.md
└── setup.py
```

Adesso apriamo la cartella **dist** e qui abbiamo tutto il necessario preparato per caricare il nostro pacchetto sul repositorio di PyPi.

# 3) Pubblicazione del pacchetto

ATTENZIONE: test.pypi.org è diverso dal regolere repositorio PyPi.

Per prima cosa, carichiamo il pacchetto nel repositorio di test di PyPi. E una volta che siamo sicuri che il nostro test ha avuto successo, carichiamo il pacchetto sul repositorio di PyPi, in modo da condividerlo con tutti gli altri. In questo modo, ognuno potrà installare il nostro pacchetto semplicemente digitando  ```pip install [il_nostro_pacchetto```.

Per fare tutto ciò, è prima necessario installare un pacchetto che ci aiuti per fare tutto ciò, ovvero **twine**:
```pip install twine```.

Una volta installato, carichiamo il nostro pacchetto su test.pypi.org digitando il comando:

```
twine upload --repository-url http://test.pypi.org/legacy/ dist/*
```
Ci chiederà le credenziali di login.

L'output del comnado sarà:

```
Enter your username: lorenzomarini96
Enter your password: 
Uploading package_model-0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.8/17.8 kB • 00:00 • 12.7 MB/s

View at:
https://test.pypi.org/project/package-model/0.1/
```

Controlliamo se il pacchetto è stato caricato su Test.PyPi, inserendo il link generato dal comando precedente su Terminale.

Inseriamo su Terminale il comando creato per installare il nostro pacchetto dal reposotorio di test:
pip install -i https://test.pypi.org/simple/ package-model==0.1.

Adesso siamo pronti per fare lo stesso sul repositorio regolare di PyPi. Prima di tutti, disinstalliamo il nostro pacchetto (in modo da poterlo ri-installare in seguito):

```
pip uninstall package_model
```
Carichiamo il contenuto della cartella dist per mezzo del comando seguente:

```twine upload dist/*```

Come prima, inseriamo le credenziali di login (di PyPi, non Test.PyPi!), ottenendo l'output seguente:

```
Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: lorenzomarini96
Enter your password: 
Uploading package_model-0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.8/17.8 kB • 00:00 • 13.8 MB/s

View at:
https://pypi.org/project/package-model/0.1/
```

Copiamo e incolliamo il link creato e andiamo a guardare il nostro pacchetto caricato su PyPi. Il nostro pacchetto è finalmente disponibile a tutto il mondo!
Tutti possono scaricarlo e utilizzarlo semplicemente digitando ```pip install [il_nostro_pacchetto]```.
