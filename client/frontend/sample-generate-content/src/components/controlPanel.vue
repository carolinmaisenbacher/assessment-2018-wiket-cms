<template>
  <div id="controlPanelStyle">
    <input
      v-bind:value="pageTitle"
      v-on:input="$emit('input', $event.target.value)"
      placeholder="put your title here">
    <select v-model="pageTitleBackgroundColor"
            v-bind:value="pageTitleBackgroundColor"
            v-on:input="$emit('input', $event.target.value)">
      <option disabled value="">Please select title color</option>
      <option>red</option>
      <option>green</option>
      <option>blue</option>
    </select>
    <!-- <color-picker></color-picker> -->
  </div>
</template>
<script>
  // import colorPicker from './v-color-master/src/color-picker'

  export default {
    name: 'controlPanel',
    data () {
      return{
        pageTitle: undefined,
        pageTitleBackgroundColor: undefined,
      }
    },
    components: {
      // colorPicker,
    }
  };
</script>
<style>
  #controlPanelStyle {
    width: 20%;
    height: 100%;
    background-color: grey;
    float: left;
  }
</style>
