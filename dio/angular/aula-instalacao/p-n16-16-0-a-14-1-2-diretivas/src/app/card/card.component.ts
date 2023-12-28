import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit {
  produtos: string[] = []
  menuType: string = "" 
  constructor() {
    this.produtos = [
      "mouse",
      "teclado",
      "cabo",
      "monitor",
    ]
   }

  ngOnInit(): void {
  }

  adicionar(){
    this.produtos.push("Novo");
  }
  remover(){
    this.produtos.pop();
  }
  excluir(index: number){
    this.produtos.splice(index, 1);
  }
}
