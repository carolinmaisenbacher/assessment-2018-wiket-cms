<template>
  <div id="cmsMenu">
    <div id="selectionLeft">
      <h3> Verwalte deine Speisekarte</h3>
      <cmsSelectionLeft
        state="componentClicked"
        v-bind:data="{
            title: 'Generelle Einstellungen',
            subtext: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam' }">
      </cmsSelectionLeft>
      <cmsSelectionLeft v-bind:data="{
          title: 'Warme Vorspeisen',
          subtext: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr' }">
      </cmsSelectionLeft>
    </div>
  </div>
</template>
<script>
  import cmsSelectionLeft from './cmsSelectionLeft.vue'

  export default {
    name: 'cmsMenu',
    data () {
      return{
        data: {},
      }
    },
    components: {
      cmsSelectionLeft,
    },
    methods: {
      myFilter: function(){
          this.isActive = !this.isActive;
        // some code to filter users
      }
    },
  };
</script>
<style>
  h3 {
    text-align: left;
  }
  #selectionLeft {
    width: 300px;
    margin: 0 20px;
    height: 100 %;
    position: fixed;
  }
  .componentClicked {
    background-color: blue;
  }
</style>

<!--  -->
