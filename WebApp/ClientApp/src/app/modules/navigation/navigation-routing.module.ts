import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { IntelligenceComponent } from '../intelligence/components/intelligence/intelligence.component';

const routes: Routes = [
  {
    path: '',
    component: IntelligenceComponent,
    loadChildren: () =>
      import('../intelligence/intelligence.module').then(
        (mod) => mod.IntelligenceModule
      ),
  },

  { path: '', redirectTo: '', pathMatch: 'full' },
];

@NgModule({
  imports: [[RouterModule.forChild(routes)]],
  exports: [RouterModule],
})
export class NavigationRoutingModule {}
