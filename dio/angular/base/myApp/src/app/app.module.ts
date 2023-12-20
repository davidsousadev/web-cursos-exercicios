import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { BotaoComponent } from './components/botao/botao.component';

@NgModule({
  imports:      [ BrowserModule ],
  declarations: [ AppComponent, BotaoComponent ],
  exports:      [ AppComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }