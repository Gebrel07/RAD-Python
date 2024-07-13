from django.db import models

from ..cliente.models import Cliente
from ..produto.models import Produto
from ..vendedor.models import Vendedor


class Venda(models.Model):
    vendedor = models.ForeignKey(
        to=Vendedor, on_delete=models.SET_NULL, null=True
    )
    cliente = models.ForeignKey(
        to=Cliente, on_delete=models.SET_NULL, null=True
    )
    data_venda = models.DateField(null=False, auto_now_add=True)
    parcelas_pgto = models.PositiveIntegerField(null=False, default=0)
    comissao = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return f"id: {self.id}, data_venda: {self.data_venda}"

    def total_venda(self):
        return sum(item.total_item() for item in self.itens.all())

    def total_comissao(self):
        return self.total_venda() * (self.comissao / 100)

    def get_tipo_pgto_str(self):
        if self.parcelas_pgto == 0:
            return "À vista"
        else:
            return "Parcelado"


class ItemVenda(models.Model):
    venda = models.ForeignKey(
        Venda, related_name="itens", on_delete=models.CASCADE, null=False
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False)
    preco_unitario_venda = models.DecimalField(
        max_digits=7, decimal_places=2, null=False, default=0.00
    )
    quantidade = models.PositiveIntegerField(null=False, default=1)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return (
            f"id: {self.id}, "
            f"produto_id: {self.produto.id}, "
            f"quantidade: {self.quantidade}, "
            f"valor_unitario_venda: {self.preco_unitario_venda}"
        )

    def total_item(self):
        return self.quantidade * self.produto.preco * (1 - self.desconto / 100)
