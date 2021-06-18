import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { IntelligenceComponent } from './components/intelligence/intelligence.component';

const routes: Routes = [
  // { path: '', component: AdventureListComponent },
  { path: '', component: IntelligenceComponent },

  // { path: 'combo', component: ComboActivitiesListComponent },
  // { path: '', redirectTo: 'activities', pathMatch: 'full' },
];

@NgModule({
  imports: [[RouterModule.forChild(routes)]],
  exports: [RouterModule],
})
export class IntelligenceRoutingModule {}
