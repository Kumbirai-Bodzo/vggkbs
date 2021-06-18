import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ApplicationSharedModules } from 'src/app/application-shared/modules/application-shared.module';
import { IntelligenceComponent } from './components/intelligence/intelligence.component';
import { IntelligenceRoutingModule } from './intelligence-routing.module';

@NgModule({
  imports: [CommonModule, ApplicationSharedModules, IntelligenceRoutingModule],
  declarations: [IntelligenceComponent],
})
export class IntelligenceModule {}
