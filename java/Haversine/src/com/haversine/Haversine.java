package com.haversine;

public class Haversine {
    public static double distance(double lat1, double lon1, double lat2, double lon2) {
        double R = 3959.87433;

        double dLat = Math.toRadians(lat2 - lat1);
        double dLon = Math.toRadians(lon2 - lon1);
        double lat1_r = Math.toRadians(lat1);
        double lat2_r = Math.toRadians(lat2);

        double a = Math.pow(Math.sin(dLat / 2), 2) + Math.cos(lat1_r) * Math.cos(lat2_r) * Math.pow(Math.sin(dLon / 2), 2);
        double c = 2 * Math.asin(Math.sqrt(a));
        return R * c;
    }

    public static void main(String[] args) {
        double lon1 = -103.548851;
        double lat1 = 32.0004311;
        double lon2 = -103.6041946;
        double lat2 = 33.374939;

        long t0 = java.lang.System.currentTimeMillis();
        for (int i=0; i < 10000000; i++) {
            Haversine.distance(lat1, lon1, lat2, lon2);
        }
        long t1 = java.lang.System.currentTimeMillis();
        System.out.println(t1 - t0);
    }
}
