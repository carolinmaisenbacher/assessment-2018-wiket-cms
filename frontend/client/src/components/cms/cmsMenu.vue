<template>
  <div id="cmsMenu">
    <div id="selectionLeft">
      <h3> Verwalte deine Speisekarte</h3>
      <ul>
        <li><button @click="setCssSectionActive(0)"><cmsSelectionLeft
          v-bind:class="{ cssMenuIsActive: cssSection[0], cssMenuNotActive: !cssSection[0] }"
          v-bind:data="{
              title: 'Generelle Einstellungen',
              subtext: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam' }">
        </cmsSelectionLeft></button></li>
        <li><button @click="setCssSectionActive(1)"><cmsSelectionLeft
          v-bind:class="{ cssMenuIsActive: cssSection[1], cssMenuNotActive: !cssSection[1] }"
          v-bind:data="{
            title: 'Warme Vorspeisen',
            subtext: 'Lorem ipsum dolor sit amet, consetetur sadipscing ' }">
        </cmsSelectionLeft></button></li>
        <li><button @click="setCssSectionActive(2)"><cmsSelectionLeft
          v-bind:class="{ cssMenuIsActive: cssSection[2], cssMenuNotActive: !cssSection[2] }"
          v-bind:data="{
            title: 'Kalte Vorspeisen',
            subtext: 'Lorem ipsum dolor sit amet, consetetur sadipscing ' }">
        </cmsSelectionLeft></button></li>
        <li><button @click="setCssSectionActive(3)"><cmsSelectionLeft
          v-bind:class="{ cssMenuIsActive: cssSection[3], cssMenuNotActive: !cssSection[3] }"
          v-bind:data="{
            title: 'Hauptgerichte',
            subtext: 'Lorem ipsum dolor sit amet, consetetur sadipscing ' }">
        </cmsSelectionLeft></button></li>
      </ul>
    </div>
    <div id="selectionMain">
      <cmsMenuPreferencesOverallSettings v-if="showSelection == 1"></cmsMenuPreferencesOverallSettings>
      <cmsMenuPreferencesWarmeVorspeisen v-if="showSelection == 2"></cmsMenuPreferencesWarmeVorspeisen>
      <cmsMenuPreferencesKalteVorspeisen v-if="showSelection == 3"></cmsMenuPreferencesKalteVorspeisen>
      <cmsMenuPreferencesHauptgerichte v-if="showSelection == 4"></cmsMenuPreferencesHauptgerichte>
    </div>
  </div>
</template>
<script>
  import cmsSelectionLeft from './cmsSelectionLeft.vue'
  import cmsMenuPreferencesOverallSettings from './cmsMenuPreferencesOverallSettings.vue'
  import cmsMenuPreferencesWarmeVorspeisen from './cmsMenuPreferencesWarmeVorspeisen.vue'
  import cmsMenuPreferencesKalteVorspeisen from './cmsMenuPreferencesKalteVorspeisen.vue'
  import cmsMenuPreferencesHauptgerichte from './cmsMenuPreferencesHauptgerichte.vue'

  export default {
    name: 'cmsMenu',
    data () {
      return{
        data: {},
        cssSection: [false, false, false, false],
        showSelection: 0,
      }
    },
    components: {
      cmsSelectionLeft,
      cmsMenuPreferencesOverallSettings,
      cmsMenuPreferencesWarmeVorspeisen,
      cmsMenuPreferencesKalteVorspeisen,
      cmsMenuPreferencesHauptgerichte,
    },
    methods: {
      setCssSectionActive: function(index){
        for (var i in this.cssSection){
          if (index == i){
            this.$set(this.cssSection, i, true)
          } else {
            this.$set(this.cssSection, i, false)
          }
        }
        this.showSelection = 1 + index
      }
    },
  };
</script>
<style>
  #selectionLeft ul {
    list-style-type: none;
  }
  #selectionLeft h3 {
    text-align: left;
  }
  #selectionLeft button {
    border: none;
    outline: none;
  }
  #selectionLeft {
    margin: 0 20px;
    height: 100 %;
    position: fixed;
  }
  #selectionMain {
    position: absolute;
    width: 500px;
    height: 85vh;
    top: 10vh;
    left: 430px;
    z-index: -1;
  }
  .cssMenuIsActive {
    background-color: blue;
    border-radius: 5px;
    width: 350px;
    height: 100%;
    left: 0;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
  .cssMenuNotActive {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius: 5px;
    left: 0;
    width: 300px;
  }

</style>
