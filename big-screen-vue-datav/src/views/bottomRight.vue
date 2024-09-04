<template>
  <div id="bottomRight">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="chart-area" class="text-icon"></icon>
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2"><h1 style="font-size: 27px">汽车排行榜</h1></span>
          <div class="decoration2">
            <dv-decoration-2 :reverse="true" style="width:5px;height:6rem;" />
          </div>
        </div>
      </div>
      <div class="row_list">
        <li class="car_rank_header" style="font-size: 20px; margin-top: 15px">
          <div>销售排名</div>
          <div>图片</div>
          <div>汽车信息</div>
          <div>销售价格</div>
          <div>销售趋势</div>
          <div>保修时间</div>
          <div>上市时间</div>
        </li>
        <ul class="car_rank" style="width: 100%; height: 420px; overflow: auto">
          <li v-for="car in carData" v-bind:key="carData.rank">
            <div class="list_rank">{{car.rank}}</div>
            <div class="list_img"><img :src="car.carImg" style="height: 100%; width: 100%"></div>
            <div class="list_info">
              <p>{{car.carName}}</p>
              <p>{{car.manufacturer}}/{{car.brand}}</p>
            </div>
            <div class="list_price">{{car.price}}万元</div>
            <div class="list_saleVolume">{{car.saleVolume}}辆</div>
            <div class="list_insure">{{car.insure}}</div>
            <div class="list_marketTime">{{car.marketTime}}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
// import BottomRightChart from "@/components/echart/bottom/bottomRightChart";
export default {
  data(){
    return{
      carData:''
    }
  },
  components: {
    // BottomRightChart
  },
  async mounted(){
    const res = await this.$http.get('myApp/bottomRight')
    this.carData = res.data.carData

  }
};
</script>

<style lang="scss" class>
$box-height: 520px;
$box-width: 100%;
#bottomRight {
  padding: 14px 16px;
  height: $box-height;
  width: $box-width;
  border-radius: 5px;
  .bg-color-black {
    height: $box-height - 30px;
    border-radius: 10px;
  }
  .text {
    color: #c3cbde;
  }
  //下滑线动态
  .decoration2 {
    position: absolute;
    right: 0.125rem;
  }
  .chart-box {
    margin-top: 16px;
    width: 170px;
    height: 170px;
    .active-ring-name {
      padding-top: 10px;
    }
  }
  // 列表
  .row_list {
    list-style: none;
    .car_rank::-webkit-scrollbar{
      display: none;
    }
    .car_rank li{
      display: grid;
      -ms-grid-columns: 100px 150px 180px 120px 120px 110px 100px;
      grid-template-columns: 100px 150px 180px 120px 120px 110px 100px;
      cursor: pointer;
      margin-left: 23px;
      text-align: center;
      line-height: 42px;
    }
    .car_rank .list_img{
      width: 156px;
      height: 85px;
    }
    .car_rank .list_info{
      line-height: 30px;
    }
    .car_rank .list_rank{
      line-height: 80px;
    }
    .car_rank .list_price{
      line-height: 80px;
    }
    .car_rank .list_saleVolume{
      line-height: 80px;
    }
    .car_rank .list_insure{
      line-height: 80px;
    }
    .car_rank .list_marketTime{
      line-height: 80px;
    }
    .car_rank_header {
      display: grid;
      -ms-grid-columns: 100px 150px 180px 120px 120px 110px 100px;
      grid-template-columns: 100px 150px 180px 120px 120px 110px 100px;
      margin-left: 23px;
      text-align: center;
      line-height: 30px;
      position: sticky;
      top: 0;
      z-index: 1; /* 确保标题行在其他内容之上 */
    }
  }
}
</style>