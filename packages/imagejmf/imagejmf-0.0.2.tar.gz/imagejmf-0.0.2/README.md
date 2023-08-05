
# Package Name
### imagejmf

O pacote image-processing-joelmaf é usado para processare imagem. É composto de dois módulos:
- Módulo "Processing":
  - Correspondência de histograma;
  - Similaridade estrutural;
  - Redimensionar imagem;
- Módulo "Utils":
  - Ler imagem;
  - Salvar imagem;
  - Plotar imagem;
  - Resultado do gráfico;
  - Plotar histograma;

### Instalção do Pacote
```
pip install imagejmf
```

## Uso

```python
from imagejmf.processing import combination
combination.find_difference(image1, image2)
```

## Autor
Joelma de Moura Ferreira

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
