import { NgModule } from '@angular/core';
import { AvatarModule } from 'primeng/avatar';
import { AvatarGroupModule } from 'primeng/avatargroup';
import { BadgeModule } from 'primeng/badge';
import { BreadcrumbModule } from 'primeng/breadcrumb';
import { CalendarModule } from 'primeng/calendar';
import { CarouselModule } from 'primeng/carousel';
import { CheckboxModule } from 'primeng/checkbox';
import { ChipsModule } from 'primeng/chips';
import { DataViewModule } from 'primeng/dataview';
import { DialogModule } from 'primeng/dialog';
import { DropdownModule } from 'primeng/dropdown';
import { FileUploadModule } from 'primeng/fileupload';
import { GalleriaModule } from 'primeng/galleria';
import { InputNumberModule } from 'primeng/inputnumber';
import { InputSwitchModule } from 'primeng/inputswitch';
import { KeyFilterModule } from 'primeng/keyfilter';
import { LightboxModule } from 'primeng/lightbox';
import { MenuModule } from 'primeng/menu';
import { MenubarModule } from 'primeng/menubar';
import { MessageModule } from 'primeng/message';
import { MessagesModule } from 'primeng/messages';
import { MultiSelectModule } from 'primeng/multiselect';
import { OrderListModule } from 'primeng/orderlist';
import { OverlayPanelModule } from 'primeng/overlaypanel';
import { PanelModule } from 'primeng/panel';
import { RadioButtonModule } from 'primeng/radiobutton';
import { ScrollTopModule } from 'primeng/scrolltop';
import { SelectButtonModule } from 'primeng/selectbutton';
import { SidebarModule } from 'primeng/sidebar';
import { SkeletonModule } from 'primeng/skeleton';
import { SliderModule } from 'primeng/slider';
import { SplitButtonModule } from 'primeng/splitbutton';
import { TableModule } from 'primeng/table';
import { TabMenuModule } from 'primeng/tabmenu';
import { TagModule } from 'primeng/tag';
import { ToggleButtonModule } from 'primeng/togglebutton';
import { TooltipModule } from 'primeng/tooltip';
@NgModule({
  exports: [
    FileUploadModule,
    ScrollTopModule,
    TagModule,
    ToggleButtonModule,
    BadgeModule,
    AvatarGroupModule,
    AvatarModule,
    SkeletonModule,
    // MenuModule,
    MenubarModule,
    SidebarModule,
    InputNumberModule,
    MessagesModule,
    MessageModule,
    GalleriaModule,
    OverlayPanelModule,
    OrderListModule,
    CarouselModule,
    TabMenuModule,
    MenuModule,
    ChipsModule,
    SelectButtonModule,
    MultiSelectModule,
    SliderModule,
    TableModule,
    BreadcrumbModule,
    DropdownModule,
    CalendarModule,
    TooltipModule,
    InputSwitchModule,
    LightboxModule,
    DialogModule,
    KeyFilterModule,
    SplitButtonModule,
    RadioButtonModule,
    CheckboxModule,
    PanelModule,
    DataViewModule,
  ],

  // declarations:[ToSelectItemPipe]
})
export class PrimengSharedModules {}
