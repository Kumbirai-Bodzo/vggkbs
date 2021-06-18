import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PageNotFoundComponent } from './application-shared/components/page-not-found/page-not-found.component';
import { NavigationComponent } from './modules/navigation/components/navigation/navigation.component';
// import { AuthenticationComponent } from './modules/authentication/authentication.component';
//import { LoginComponent } from './modules/authentication/components/login/login.component';

const routes: Routes = [
  // { path: '', component: NavigationComponent },

  // { path: '**', redirectTo: 'google', pathMatch: 'full' },

  {
    path: '',
    component: NavigationComponent,
    loadChildren: () =>
      import('./modules/navigation/navigation.module').then(
        (mod) => mod.NavigationModule
      ),
  },

  // {
  //   path: 'login',
  //   component: LoginComponent,
  //   outlet: 'modal',
  // },

  // 404 pageaccommodation
  { path: '**', component: PageNotFoundComponent },

  /*
  {
    path: 'auth',
    component: NavigationComponent,
    loadChildren: () =>
      import('./modules/authentication/AuthenticationModule').then(
        (mod) => mod.AuthenticationModule
      ),
  },*/

  {
    path: 'bookings',
    runGuardsAndResolvers: 'always',
    // canActivate: [AuthGuard],
    children: [
      //  { path: '', component: BookingsComponent },
      //  { path: 'create', component: BookingCreateComponent },
      //  { path: 'update/:id', component: BookingUpdateComponent },
    ],
  },
  { path: '**', redirectTo: '', pathMatch: 'full' },
  // { path: 'help', component: HelpComponent },
  // { path: 'login', component: AuthenticationComponent },
  // { path: 'adventure/gallery/:id', component: GalleryComponent },
  // { path: 'adventure', component: AdventureComponent },
  // { path: 'logout', component: AdventureComponent },
  // { path: '**', redirectTo: '', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
