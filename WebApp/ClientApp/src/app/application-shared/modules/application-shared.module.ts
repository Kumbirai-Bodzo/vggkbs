import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { PrimengSharedModules } from './primeng-shared.module';
import { SharedComponentsModule } from './shared-components.module';
import { SharedPipesModule } from './shared-pipes.module';

@NgModule({
  exports: [
    PrimengSharedModules,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    SharedPipesModule,
    SharedComponentsModule,
    // VideogularModule,
    // BookingModule,
  ],

  // declarations:[ToSelectItemPipe]
})
export class ApplicationSharedModules {}
/*

 providers: [
    {
      provide: 'SocialAuthServiceConfig',
      useValue: {
        autoLogin: true,
        providers: [
          {
            id: GoogleLoginProvider.PROVIDER_ID,
            provider: new GoogleLoginProvider(
              '624796833023-clhjgupm0pu6vgga7k5i5bsfp6qp6egh.apps.googleusercontent.com'
            ),
          },

        ],
      } as SocialAuthServiceConfig,
    }
  ],

*/
