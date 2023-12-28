import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-comp-atributos',
  templateUrl: './comp-atributos.component.html',
  styleUrls: ['./comp-atributos.component.css']
})
export class CompAtributosComponent implements OnInit {
  estilo: string = "disable"
  corfundo = "blue"
  corfont = "pink"
  item:string = ""
  lista:string[] = []
  isEnableBlock:boolean = true
  constructor() { }
  adicionarLista(){
    this.lista.push(this.item)
  }
  trocarCor(){
    if (this.estilo==="enable"){
      this.estilo = "disable";
    }
    else{
      this.estilo = "enable";
    }
  }

  trocaestilo(){
    if (this.corfundo==="red"){
      this.corfundo = "blue";
    }
    else{
      this.corfundo = "red";
    }
  }
  trocafont(){
    if (this.corfont==="pink"){
      this.corfont = "green";
    }
    else{
      this.corfont = "pink";
    }
  }
  ngOnInit(): void {
  }

}
