import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { IntelligenceComponent } from './components/intelligence/intelligence.component';

const routes: Routes = [
  { path: '', component: IntelligenceComponent },
];

@NgModule({
  imports: [[RouterModule.forChild(routes)]],
  exports: [RouterModule],
})
export class IntelligenceRoutingModule {}
