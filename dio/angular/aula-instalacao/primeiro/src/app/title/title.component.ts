import { Component } from '@angular/core';
import {AppComponent} from '../app.component';
@Component({
  selector: 'app-title',
  standalone: true,
  imports: [AppComponent],
  templateUrl: './title.component.html',
  styleUrl: './title.component.css'
})
export class TitleComponent {

}
