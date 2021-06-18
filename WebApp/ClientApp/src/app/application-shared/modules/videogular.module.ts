import { NgModule } from '@angular/core';
import { VgBufferingModule, VgControlsModule, VgCoreModule, VgOverlayPlayModule } from 'ngx-videogular';

// import { VgCoreModule } from '@videogular/ngx-videogular/core';
@NgModule({
  exports: [
    VgCoreModule,
    VgControlsModule,
    VgOverlayPlayModule,
    VgBufferingModule,
  ],
})
export class VideogularModule {}
