import { Component, OnInit } from '@angular/core';
import { info } from '../../../application-shared/constants/info';

@Component({
  selector: 'app-page-not-found',
  templateUrl: './page-not-found.component.html',
  styleUrls: ['./page-not-found.component.scss'],
})
export class PageNotFoundComponent implements OnInit {
  public info: any;
  constructor() {}

  ngOnInit() {
    this.info = info;
  }
}
