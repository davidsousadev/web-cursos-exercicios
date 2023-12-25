import { Component, Input,OnChanges, OnDestroy, OnInit,  } from '@angular/core';

@Component({
  selector: 'app-botao',
  standalone: true,
  imports: [],
  templateUrl: './botao.component.html',
  styleUrl: './botao.component.css'
})
export class BotaoComponent implements OnDestroy, OnInit, OnChanges {
  @Input() nome:string = '';
  constructor(){
    console.log(`Construiu ${this.nome}`);
  }
  ngOnDestroy(): void {
    console.log("Destruido ", this.nome);
  }
  ngOnChanges(): void {
    console.log(`Alterou ${this.nome}`);
  }
  ngOnInit(): void {
    console.log(`Botao Nasceu ${this.nome}`);
  }
}
